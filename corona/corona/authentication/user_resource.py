# -*- coding: utf-8 -*-

"""
    MongoDB Resource Authentication

"""

from mongoengine import *

from webapp.models import User
from webapp.models import Counselor
from webapp.models import Student
from webapp.models import TaskGroup

import user_auth
import logging

def taskgroup(request, args):

    try:
        input = request.DATA
        cookie = request.COOKIES

        op_uid = cookie['userid']

        if request.method == 'POST':

            if input['userid'] == op_uid:
                return True
            else:
                if not user_auth.is_counselor(op_uid):
                    return False
                counselor = Counselor.objects(pk=op_uid).first()
                if not input['userid'] in counselor.student_id_list:
                    return False
                return True

        if request.method == 'GET':

            if args[0] == 'object':
                obj_id = args[1]
                taskgroup = TaskGroup.objects(pk=obj_id).first()
                owner_id = taskgroup.task_owner_id
                if user_auth.is_counselor(op_uid):
                    counselor = Counselor.objects(pk=op_uid).first()
                    if owner_id in counselor.student_id_list:
                        return True

                elif user_auth.is_student(op_uid):
                    student = Student.objects(pk=op_uid).first()
                    if str(student.id) == owner_id:
                        return True

            elif args[0] == 'user':
                userid = args[1]
                if userid == op_uid:
                    return True
                else:
                    if user_auth.is_counselor(op_uid):
                        counselor = Counselor.objects(pk=op_uid).first()
                        if userid in counselor.student_id_list:
                            return True
            return False

        if request.method == 'PUT':

            obj_id = input['taskgroup']
            taskgroup = TaskGroup.objects(pk=obj_id).first()
            owner_id = taskgroup.task_owner_id
            if user_auth.is_counselor(op_uid):
                counselor = Counselor.objects(pk=op_uid).first()
                if owner_id in counselor.student_id_list:
                    return True
            return False

        if request.method == 'DELETE':

            if args[0] == 'object':
                obj_id = args[1]
                taskgroup = TaskGroup.objects(pk=obj_id).first()
                owner_id = taskgroup.task_owner_id
                if user_auth.is_counselor(op_uid):
                    counselor = Counselor.objects(pk=op_uid).first()
                    if owner_id in counselor.student_id_list:
                        return True
                return False
            else:
                return False

    except Exception, e:
        logging.getLogger("general").debug(e)
        return False



def task(request, args):

    try:
        if (args[0] == 'object') and (not args[1] == None):
            task = Task.objects(pk=args[1]).first()
            taskgroup_id = task.taskgroup_id
            args[1] = str(taskgroup_id)

        request.DATA['userid'] = request.DATA['owner']
        return taskgroup(request, args)
    except Exception,e:
        logging.getLogger("general").debug(e)
        return False

comment_types = {
    'post' : 0,
    'task' : 1
}

def comment(request, args=None):

    try:
        input = request.DATA
        cookie = request.COOKIES
        userid = cookie['userid']

        if args == None:
            o_id = input['owner']
            comment_type = int(input['comment_type'])
        else:
            o_id = args[0]
            comment_type = int(args[1])

        if comment_type == comment_types['post']:
            
            # need to add logic
            return True

        elif comment_type == comment_types['task']:
            
            task = Task.objects(pk=o_id).first()
            people = task.associate_owner_list
            people.append(task.owner)
            
            if userid in people:
                return True
            return False

    except Exception, e:
        return False

def post(request, args=None):

    try:

        input = request.DATA
        cookie = request.COOKIES
        userid = cookie['userid']

        if request.method == 'PUT':
            obj_id = input['post']
            post = Post.objects(pk=obj_id).first()
            if userid == post.owner:
                return True

        if request.method == 'GET':
            if args[0] == 'object':
                obj_id = args[1]
                if obj_id:
                    post = Post.objects(pk=obj_id).first()
                    if userid == post.owner:
                        return True
        return False
    except Exception, e:
        return False




















