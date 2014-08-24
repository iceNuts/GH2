# -*- coding: utf-8 -*-

from django.views.decorators.csrf import csrf_exempt

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.core.cache import cache
from corona.settings import SECRET_KEY

from webapp.viewmodels import userviewmodel
from utilities.custom_decorators import user_login_required
from django.core.exceptions import ValidationError

import logging
import json
import hashlib
from datetime import datetime
from random import randint

header = dict()
header['CharSet'] = 'unicode'

@csrf_exempt
@api_view(['POST'])
def user_login(request):

    try:

        output = userviewmodel.login_post(request.DATA)
        response = Response({'userid' : output['userid'], 'token': output['token']}, headers=header, status=status.HTTP_200_OK)

        response.set_cookie('userid', output['userid'])
        response.set_cookie('token', output['token'])

        return response

    except Exception, e:
        logging.getLogger("general").debug(e)
        return Response(json.dumps({'error_code' : 'error'}), status=status.HTTP_403_FORBIDDEN)

@csrf_exempt
@api_view(['GET'])
@user_login_required
def user(request, uid=None):

    try:
        output = userviewmodel.user_get({ 'uid' : uid})

        return Response({'result' : output}, status=status.HTTP_200_OK)

    except Exception, e:
        logging.getLogger("general").debug(e)
        return Response(json.dumps({'error_code' : 'error'}), status=status.HTTP_500_INTERNAL_SERVER_ERROR)














