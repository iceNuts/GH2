# -*- coding: utf-8 -*-

"""
    MVVM
    Activity View Model

"""

import logging
import datetime
import re
import hashlib

from webapp.models import Student
from webapp.models import Parent
from webapp.models import Counselor
from webapp.models import CounselorAdmin
from webapp.models import User
from webapp.models import Event
from webapp.models import Alert
from webapp.models import Activity
from webapp.models import CachedObject

from datetime import datetime
from random import randint
from corona.settings import SECRET_KEY
from corona.settings import ACTIVATE_KEY


from django.core.exceptions import ValidationError
from django.core.cache import cache
from utilities import rqjob
from utilities import my_json

import logging

activity_types = {
    'post' :        0,      # 添加/修改了 post
    'comment' :     1,      # 评论了
    'appfile' :     2,      # 上传了
    'task' :        3,      # 添加了task 修改了task
    'deadline' :    4,      # deadline(task)  (服务器/Mobile)发生当天有提醒 （Mobile)提前两天
    'taskgroup' :   8,      # TaskGroup Info

    'counselor' :   101,      # Counselor Change
    'school' :      102,      # School Change
}

system_limit = 300



""" TYPE API """


"""
    Get activity update list from timestamp by limit

"""

def type_activity_by_limit(input, userid):

    limit = int(input['limit'])
    revert = input['revert']
    activity_type = input['type']

    cache_key = userid+activity_type+'limit'

    if int(revert) == 1:
        revert = True
    else:
        revert = False 

    timestamp = datetime.fromtimestamp(float(input['timestamp']))

    cached_object = cache.get(cache_key)

    if not cached_object == None:
        activities = cached_object.get_by_limit(timestamp, limit, revert=revert)
        if not activities == None:
            activity_list = []
            for a in activities:
                a = a.to_mongo()
                a = my_json.clean_bson(a)
                activity_list.append(a)
            return activity_list
        else:
            # this cache expires
            cache.delete(cache_key)

    cached_object = CachedObject(cache_key)

    activities = Activity.objects(user_id=userid, activity_type=activity_types[activity_type], update_time__lt=timestamp, read=0)
    # activities = sorted(activities, key=operator.attrgetter('update_time'), reverse=True)

    activities = activities[:system_limit]

    cached_key = cached_object.put(activities, timestamp)

    activities = activities[:limit]

    cache.set(cached_key, cached_object, 60*10)

    activity_list = []
    for a in activities:
        a = a.to_mongo()
        a = my_json.clean_bson(a)
        activity_list.append(a)

    output = activity_list

    return output

"""
    Get activity update list from timestamp0 to timestamp1

"""

def type_activity_by_timestamp(input, userid):

    activity_type = input['type']

    cache_key = userid+activity_type+'timestamp'

    from_timestamp = datetime.fromtimestamp(float(input['from_timestamp']))
    end_timestamp = datetime.fromtimestamp(float(input['end_timestamp']))

    cached_object = cache.get(cache_key)

    if from_timestamp > end_timestamp:
        return None

    if not cached_object == None:
        activities = cached_object.get_by_timestamp(from_timestamp, end_timestamp)
        if not activities == None:
            activity_list = []
            for a in activities:
                a = a.to_mongo()
                a = my_json.clean_bson(a)
                activity_list.append(a)
            return activity_list
        else:
            # this cache expires
            cache.delete(cache_key)

    cached_object = CachedObject(cache_key)

    activities = Activity.objects(user_id=userid, activity_type=activity_types[activity_type], update_time__lt=end_timestamp, read=0)
    # activities = sorted(activities, key=operator.attrgetter('update_time'), reverse=True)

    activities = activities[:system_limit]
    cached_key = cached_object.put(activities, from_timestamp, end_timestamp)

    activity_list = []
    for a in activities:
        if a.update_time >= from_timestamp:
            a = a.to_mongo()
            a = my_json.clean_bson(a)
            activity_list.append(a)

    cache.set(cached_key, cached_object, 60*5)

    output = activity_list

    return output



""" PRIORITY API """


"""
    Get activity update list from timestamp by limit

"""

low_types = [
    1, 101, 102
]

high_types = [
    0, 2, 3, 4, 8
]

def priority_activity_by_limit(input, userid):

    limit = int(input['limit'])
    revert = input['revert']
    priority = str(input['priority'])

    cache_key = userid+priority+'limit'

    if int(revert) == 1:
        revert = True
    else:
        revert = False 

    timestamp = datetime.fromtimestamp(float(input['timestamp']))

    cached_object = cache.get(cache_key)

    if not cached_object == None:
        activities = cached_object.get_by_limit(timestamp, limit, revert=revert)
        if not activities == None:
            activity_list = []
            for a in activities:
                a = a.to_mongo()
                a = my_json.clean_bson(a)
                activity_list.append(a)
            return activity_list
        else:
            # this cache expires
            cache.delete(cache_key)

    cached_object = CachedObject(cache_key)

    if priority == '0':
        type_list = low_types
    else:
        type_list = high_types

    activities = Activity.objects(user_id=userid, activity_type__in=type_list, update_time__lt=timestamp, read=0)
    # activities = sorted(activities, key=operator.attrgetter('update_time'), reverse=True)

    activities = activities[:system_limit]

    cached_key = cached_object.put(activities, timestamp)

    activities = activities[:limit]

    cache.set(cached_key, cached_object, 60*10)

    activity_list = []
    for a in activities:
        a = a.to_mongo()
        a = my_json.clean_bson(a)
        activity_list.append(a)

    output = activity_list
    return output

"""
    Get activity update list from timestamp0 to timestamp1

"""

def priority_activity_by_timestamp(input, userid):

    priority = str(input['priority'])

    cache_key = userid+priority+'timestamp'

    from_timestamp = datetime.fromtimestamp(float(input['from_timestamp']))
    end_timestamp = datetime.fromtimestamp(float(input['end_timestamp']))

    cached_object = cache.get(cache_key)

    if from_timestamp > end_timestamp:
        return None

    if not cached_object == None:
        activities = cached_object.get_by_timestamp(from_timestamp, end_timestamp)
        if not activities == None:
            activity_list = []
            for a in activities:
                a = a.to_mongo()
                a = my_json.clean_bson(a)
                activity_list.append(a)
            return activity_list
        else:
            # this cache expires
            cache.delete(cache_key)

    cached_object = CachedObject(cache_key)

    if priority == '0':
        type_list = low_types
    else:
        type_list = high_types

    activities = Activity.objects(user_id=userid, activity_type__in=type_list, update_time__lt=end_timestamp, read=0)
    # activities = sorted(activities, key=operator.attrgetter('update_time'), reverse=True)

    activities = activities[:system_limit]
    cached_key = cached_object.put(activities, from_timestamp, end_timestamp)

    activity_list = []
    for a in activities:
        if a.update_time >= from_timestamp:
            a = a.to_mongo()
            a = my_json.clean_bson(a)
            activity_list.append(a)

    cache.set(cached_key, cached_object, 60*5)

    output = activity_list
    return output





funcs = {
    '0' : type_activity_by_limit,
    '1' : type_activity_by_timestamp,
    '2' : priority_activity_by_limit,
    '3' : priority_activity_by_timestamp,
}



def activity(input, userid):

    func_type = input['func_type']
    return funcs[func_type](input, userid)

def activity_read_status(input, userid):

    try:
        activities = input['activities']
        
        for a in activities:
            activity = Activity.objects(pk=a, user_id=userid)
            if not activity == None:
                activity.update(
                    set__read=1
                    )
                
    except Exception, e:
        raise ValidationError('2000')






















