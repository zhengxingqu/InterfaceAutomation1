# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .serializers import UserSerializer, ProjectSerializer, CaseSerializer
from .models import User, Project, Case
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from . import logfile
import logging
from rest_framework import filters, viewsets, mixins

logger = logging.getLogger(__name__)


# Create your views here.
# 查询、新增project接口
class InterfaceProject(generics.ListCreateAPIView):
    queryset = Project.objects.filter(isdelete=True)
    serializer_class = ProjectSerializer


class InterfaceCase(generics.ListCreateAPIView):
    queryset = Case.objects.filter(isdelete=True)
    serializer_class = CaseSerializer


class UpdateProject(generics.RetrieveUpdateAPIView):
    queryset = Project.objects.filter(isdelete=True)
    serializer_class = ProjectSerializer


class UpdateCase(generics.RetrieveUpdateAPIView):
    queryset = Case.objects.filter(isdelete=True)
    serializer_class = CaseSerializer


class DeleteProject(generics.RetrieveDestroyAPIView):
    queryset = Project.objects.filter(isdelete=True)
    serializer_class = ProjectSerializer

    def perform_destroy(self, instance):
        Project.objects.filter(id=instance.id).update(isdelete=False)


class DeleteCase(generics.RetrieveDestroyAPIView):
    queryset = Case.objects.filter(isdelete=True)
    serializer_class = CaseSerializer

    def perform_destroy(self, instance):
        Case.objects.filter(id=instance.id).update(isdelete=False)


class DeleteProjects(APIView):
    queryset = Project.objects.filter(isdelete=True)
    serializer_class = ProjectSerializer

    def put(self, request):
        return_message = {'code': 200, 'message': '成功'}

        data = request.data
        for i in data["ids"]:
            try:
                log = logfile
                Project.objects.filter(id=i).update(isdelete=False)
            except Exception:
                logger.info('删除的对象不存在')
        return Response(return_message)


class DeleteCases(APIView):
    queryset = Case.objects.filter(isdelete=True)
    serializer_class = CaseSerializer

    def put(self, request):
        return_message = {'code': 200, 'message': '成功'}

        data = request.data
        for i in data["ids"]:
            try:
                log = logfile
                Case.objects.filter(id=i).update(isdelete=False)
            except Exception:
                logger.info('删除的对象不存在')
        return Response(return_message)


# 搜索固定地址、项目名
class SearchProject(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Project.objects.filter(isdelete=True)
    serializer_class = ProjectSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('project_name', 'permanent_address')


# 搜索固定地址、项目名
class SearchCase(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Case.objects.filter(isdelete=True)
    serializer_class = CaseSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('case_name', 'case_result')
