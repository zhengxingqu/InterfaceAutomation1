# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .serializers import UserSerializer, ProjectSerializer, CaseSerializer
from .models import User, Project, Case
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from myapp.common import RestonMessage
import logging
from rest_framework import status
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

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        t = self.perform_destroy(instance)
        if t.status_code == 404:
            return Response(RestonMessage.respon_404(),
                            status=status.HTTP_404_NOT_FOUND)
        elif t.status_code == 417:
            return Response(RestonMessage.respon_417(),
                            status=status.HTTP_417_EXPECTATION_FAILED)
        else:
            return Response(RestonMessage.respon_204(),
                            status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):

        try:
            exist_project = Case.objects.filter(isdelete=True,
                                                project_name_id=instance.id)
            if exist_project:
                return Response(RestonMessage.respon_417(),
                                status=status.HTTP_417_EXPECTATION_FAILED)
            else:
                Project.objects.filter(id=instance.id).update(isdelete=False)
                logger.info('删除project对象')
                return Response(status=status.HTTP_204_NO_CONTENT)
        except Project.DoesNotExist:
            return Response('被删除的对象不存在', status=status.HTTP_404_NOT_FOUND)


class DeleteCase(generics.RetrieveDestroyAPIView):
    queryset = Case.objects.filter(isdelete=True)
    serializer_class = CaseSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        t = self.perform_destroy(instance)
        if t.status_code == 404:
            return Response(RestonMessage.respon_404(),
                            status=status.HTTP_404_NOT_FOUND)
        elif t.status_code == 417:
            return Response(RestonMessage.respon_417(),
                            status=status.HTTP_417_EXPECTATION_FAILED)
        else:
            return Response(RestonMessage.respon_204(),
                            status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        try:
            exist_id = '[' + str(instance.id) + ']'
            exist_cases = Case.objects.filter(isdelete=True,
                                              invoking_other_interface=exist_id)
            if exist_cases:
                return Response(RestonMessage.respon_417(),
                                status=status.HTTP_417_EXPECTATION_FAILED)
            else:
                Case.objects.filter(id=instance.id).update(isdelete=False)
                return Response(status=status.HTTP_204_NO_CONTENT)

        except Exception as e:
            return Response(logger.info('删除的对象不存在'))


class DeleteProjects(APIView):
    queryset = Project.objects.filter(isdelete=True)
    serializer_class = ProjectSerializer

    def put(self, request):
        return_message = {'code': 200, 'message': '成功'}

        data = request.data
        for i in data["ids"]:
            try:
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


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.filter(isdelete=True)
    serializer_class = UserSerializer


class SearchUser(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = User.objects.filter(isdelete=True)
    serializer_class = UserSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('username', 'iphone')


class UpdateUser(generics.RetrieveUpdateAPIView):
    queryset = User.objects.filter(isdelete=True)
    serializer_class = UserSerializer


class DeleteUser(generics.RetrieveDestroyAPIView):
    queryset = User.objects.filter(isdelete=True)
    serializer_class = UserSerializer

    def perform_destroy(self, instance):
        User.objects.filter(id=instance.id).update(isdelete=False)


class DeleteUsers(APIView):
    queryset = Case.objects.filter(isdelete=True)
    serializer_class = UserSerializer

    def put(self, request):
        return_message = {'code': 200, 'message': '成功'}

        data = request.data
        for i in data["ids"]:
            try:
                User.objects.filter(id=i).update(isdelete=False)
            except Exception:
                logger.info('删除的对象不存在')
        return Response(return_message)


class ResetPwd(APIView):
    serializer_class = UserSerializer
    queryset = User.objects.filter(isdelete=False)

    def put(self, request, *args, **kwargs):
        data = request.data
        # hash = hashlib.sha1()
        try:
            # hash.update(bytes(data['password']))
            # password = hash.hexdigest()
            t = User.objects.get(id=data['id'])
            t.set_password(data['password'])
            t.save()
        except Exception as e:
            logging.exception(e)
        return Response(data, status=status.HTTP_200_OK)