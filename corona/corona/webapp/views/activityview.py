# -*- coding: utf-8 -*-

from django.views.decorators.csrf import csrf_exempt

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.core.cache import cache
from corona.settings import SECRET_KEY

from webapp.viewmodels import activityviewmodel
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


"""
    Activity APIs

"""

@csrf_exempt
@api_view(['POST'])
@user_login_required
def activity(request):

    try:

        output = 'OK'

        if request.method == 'POST':
            output = activityviewmodel.activity(request.DATA, request.COOKIES['userid'])

        if request.method == 'PUT':
            activityviewmodel.activity_read_status(request.DATA, request.COOKIES['userid'])

        return Response({'result' : output}, headers=header, status=status.HTTP_200_OK)
    except Exception, e:
        logging.getLogger("general").debug(e)
        err_msg = e.messages
        return Response(json.dumps({'error_code' : err_msg}), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


























