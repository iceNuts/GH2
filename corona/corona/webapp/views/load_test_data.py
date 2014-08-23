# -*- coding: utf-8 -*-

from django.views.decorators.csrf import csrf_exempt

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.core.cache import cache
from corona.settings import SECRET_KEY

from webapp import User

from utilities.custom_decorators import user_login_required
from django.core.exceptions import ValidationError

import logging
import json
import hashlib
from datetime import datetime
from random import randint
from utilities import rqjob

header = dict()
header['CharSet'] = 'unicode'

@csrf_exempt
@api_view(['POST'])
@user_login_required
def load(request):

    db = connect('corona')
    
    db.drop_database('corona')

    li = User(
        user_name='li',
        user_password='123',
        title='looper',
        weight=2
        )
    li.save()

    yi = User(
        user_name='yi',
        user_password='123',
        title='killer',
        weight=3       
        )
    yi.save()

    gongxia = User(
        user_name='gongxia',
        user_password='123',
        title='player',
        weight=1
        )
    gongxia.save()

    chuan = User(
        user_name='chuan',
        user_password='123',
        title='looper',
        weight=2
        )
    chuan.save()

    























