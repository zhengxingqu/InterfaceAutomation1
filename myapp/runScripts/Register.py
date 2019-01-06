# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from myapp.serializers import UserSerializer
from myapp.models import User
from rest_framework import generics
import logging
from rest_framework.response import Response
from rest_framework import status
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication


# Create your views here.


# 用户注册
class Register(generics.ListCreateAPIView):
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    serializer_class = UserSerializer
    queryset = User.objects.filter(isdelete=True)

    def create(self, request, *args, **kwargs):
        data = request.data
        try:
            # 创建用户信息

            print(type(data['username']), type(data['sex']),
                  type(data['iphone']))

            User.objects.create_user(username=data['username'],
                                     password=data['password'],
                                     sex=data['sex'], iphone=data['iphone'],
                                     head_portrait=data['head_portrait']
                                     )
            return Response(data, status=status.HTTP_201_CREATED)
        except Exception as e:
            logging.exception(e)
            return Response(e)
