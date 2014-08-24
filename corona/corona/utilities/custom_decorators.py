# -*- coding: utf-8 -*-

from django.http import HttpResponse, HttpResponseRedirect
from rest_framework.response import Response
from rest_framework import status

from django.core.cache import cache

import logging
import hashlib

def user_login_required(f):
    def wrap(request, *args, **kwargs):
        try:
            user_id = request.COOKIES['userid']
            token = request.COOKIES['token']

            if not (user_id and cache.get(user_id) == token):
                return Response({'error_code' : 'not logged in'}, status.HTTP_401_UNAUTHORIZED)
        except Exception, e:
            return Response({'error_code' : 'exception'}, status.HTTP_401_UNAUTHORIZED)
        return f(request, *args, **kwargs)
    return wrap
