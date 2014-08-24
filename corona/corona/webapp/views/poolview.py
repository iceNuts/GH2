# -*- coding: utf-8 -*-

from django.views.decorators.csrf import csrf_exempt

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.core.cache import cache
from corona.settings import SECRET_KEY

from webapp.viewmodels import poolviewmodel
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
@api_view(['GET'])
@user_login_required
def popular_list(request):

    try:
        output = poolviewmodel.popular_list_get()

        return Response({'result' : output}, status=status.HTTP_200_OK)

    except Exception, e:
        logging.getLogger("general").debug(e)
        return Response(json.dumps({'error_code' : 'error'}), status=status.HTTP_500_INTERNAL_SERVER_ERROR)



@csrf_exempt
@api_view(['GET'])
@user_login_required
def pool_list(request, uid=None):

    try:

        if request.method == 'GET':
            output = poolviewmodel.pool_list_get(uid)

        return Response({'result' : output}, status=status.HTTP_200_OK)

    except Exception, e:
        logging.getLogger("general").debug(e)
        return Response(json.dumps({'error_code' : 'error'}), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@csrf_exempt
@api_view(['POST', 'GET', 'PUT', 'DELETE'])
@user_login_required
def taxonomy(request, object_id=None):

    try:

        output = 'OK'

        if request.method == 'POST':
            poolviewmodel.taxonomy_post(request.DATA)

        if request.method == 'GET':
            output = poolviewmodel.taxonomy_get(object_id)

        if request.method == 'PUT':
            poolviewmodel.taxonomy_put(request.DATA)

        if request.method == 'DELETE':
            poolviewmodel.taxonomy_delete(object_id)

        return Response({'result' : output}, status=status.HTTP_200_OK)

    except Exception, e:
        logging.getLogger("general").debug(e)
        return Response(json.dumps({'error_code' : 'error'}), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@csrf_exempt
@api_view(['POST'])
@user_login_required
def like_taxonomy(request):

    try:
        output = 'OK'

        poolviewmodel.like_taxonomy(request.DATA)

        return Response({'result' : output}, status=status.HTTP_200_OK)

    except Exception, e:
        logging.getLogger("general").debug(e)
        return Response(json.dumps({'error_code' : 'error'}), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@csrf_exempt
@api_view(['POST'])
@user_login_required
def publish_taxonomy(request):
    try:
        output = 'OK'

        poolviewmodel.publish_taxonomy(request.DATA)
        
        return Response({'result' : output}, status=status.HTTP_200_OK)
    
    except Exception, e:
        logging.getLogger("general").debug(e)
        return Response(json.dumps({'error_code' : 'error'}), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@csrf_exempt
@api_view(['POST', 'GET', 'PUT', 'DELETE'])
@user_login_required
def attribute(request, taxonomy_id=None):

    try:

        output = 'OK'

        if request.method == 'POST':
            poolviewmodel.attribute_post(request.DATA)

        if request.method == 'GET':
            output = poolviewmodel.attribute_get(taxonomy_id)

        if request.method == 'PUT':
            poolviewmodel.attribute_put(request.DATA)

        return Response({'result' : output}, status=status.HTTP_200_OK)

    except Exception, e:
        logging.getLogger("general").debug(e)
        return Response(json.dumps({'error_code' : 'error'}), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@csrf_exempt
@api_view(['POST'])
@user_login_required
def fork_taxonomy(request):

    try:
        output = 'OK'

        poolviewmodel.fork_taxonomy(request.DATA, request.DATA['userid'])

        return Response({'result' : output}, status=status.HTTP_200_OK)

    except Exception, e:
        logging.getLogger("general").debug(e)
        return Response(json.dumps({'error_code' : 'error'}), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@csrf_exempt
@api_view(['GET'])
@user_login_required
def export_taxonomy(request, taxonomy_id):

    try:

        output = poolviewmodel.export_taxonomy(taxonomy_id)

        return Response({'result' : output}, status=status.HTTP_200_OK)
    except Exception, e:
        logging.getLogger("general").debug(e)
        return Response(json.dumps({'error_code' : 'error'}), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@csrf_exempt
@api_view(['PUT'])
@user_login_required
def more_data_taxonomy(request):

    try:
        output = 'OK'
        poolviewmodel.more_data_taxonomy(request.DATA)
        return Response({'result' : output}, status=status.HTTP_200_OK)       
    except Exception, e:
        logging.getLogger("general").debug(e)
        return Response(json.dumps({'error_code' : 'error'}), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

















