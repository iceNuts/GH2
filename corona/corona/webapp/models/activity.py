# -*- coding: utf-8 -*-

"""
    Activity Model:

    fields:
        user id
        read
        activity_type
        description
        short description
        update time
        priority
        link
        dictionary

"""

from mongoengine import *

import datetime

from webapp.viewmodels.callback import update_activity


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

@update_activity.apply
class Activity(Document):

    user_id = StringField()
    read = IntField(default=0)
    activity_type = IntField()
    description = StringField()
    short_description = StringField()
    update_time = DateTimeField(default=datetime.datetime.now)
    link = StringField()
    dictionary = DictField()

    meta = {
            'indexes': 
            [
                {
                'fields': [
                        '-update_time', 
                        'user_id', 
                        'activity_type', 
                        'description',
                        'link',
                        'dictionary'
                    ]
                }
            ]
        }

















