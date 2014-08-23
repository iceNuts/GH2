# -*- coding: utf-8 -*-

"""
    MongoDB User Authentication

"""

from mongoengine import *

from webapp.models import User

import logging

user_type_options = {
    'counseloradmin': 0,
    'counselor' : 1,
    'student' : 2,
    'parent' : 4,
}


def is_admin(userid):

    try:
        user = User.objects(pk=userid).first()
        return user.user_type == user_type_options['counseloradmin']

    except Exception, e:
        return False

def is_student(userid):

    try:
        user = User.objects(pk=userid).first()
        return user.user_type == user_type_options['student']

    except Exception, e:
        return False

def is_counselor(userid):

    try:
        user = User.objects(pk=userid).first()
        return user.user_type == user_type_options['counselor']

    except Exception, e:
        return False






























