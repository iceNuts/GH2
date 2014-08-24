# -*- coding: utf-8 -*-

from django.views.decorators.csrf import csrf_exempt

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.core.cache import cache
from corona.settings import SECRET_KEY

from webapp.models import User

from utilities.custom_decorators import user_login_required
import utilities.test_data as json_data 
from django.core.exceptions import ValidationError

import logging
import json
import hashlib
from datetime import datetime
from random import randint

from mongoengine import *

header = dict()
header['CharSet'] = 'unicode'

@csrf_exempt
@api_view(['POST'])
def load(request):

    db = connect('corona')
    
    db.drop_database('corona')

    # load test data
    json_data.load()

    return Response({'result' : 'OK'}, status=status.HTTP_200_OK)

























