# -*- coding: utf-8 -*-

"""
    MVVM
    User View Model

"""

import logging
import datetime
import re
import hashlib

from webapp.models import User

from datetime import datetime
from random import randint
from corona.settings import SECRET_KEY
from corona.settings import ACTIVATE_KEY


from django.core.exceptions import ValidationError
from django.core.cache import cache
from utilities import my_json

import logging


def login_post(input):

    user_name =  input['user_name']
    user_password = input['user_password']

    user = User.objects(user_name=user_name, user_password=user_password)

    if not user == None:
        token = hashlib.md5(str(datetime.now()) + str(randint(-5000, 5000)) + SECRET_KEY).hexdigest()
        userid = str(user.first().id)

        output['userid'] = userid
        output['token'] = token

        cache.set(userid, token, 60 * 60 * 24 * 30)

        return output

    else:
        raise ValidationError('user not found')


def user_get(input):

    uid = input['uid']

    if not uid == None:

        user = User.objects(pk=uid).first()

        user = user.to_mongo()

        output = my_json.clean_bson(user)

        return output

    else:
        raise ValidationError('invalid parameter')
























