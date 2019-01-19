# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .serializers import UserSerializer, ProjectSerializer, CaseSerializer, \
    ReportSerializer, ReportDetailSerializer
from .models import User, Project, Case, Report, ReportDetail
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from myapp.common import RestonMessage
from rest_framework import status
from rest_framework import filters, viewsets, mixins
import logging
import traceback

logging.basicConfig(filename='all.txt', level=logging.INFO)


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
                logging.INFO(traceback.format_exc())
                return Response(status=status.HTTP_204_NO_CONTENT)
        except Project.DoesNotExist:
            logging.INFO(traceback.format_exc())
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

        except Exception:
            logging.INFO(traceback.format_exc())
            return Response('删除的对象不存在')


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
                logging.INFO(traceback.format_exc())
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
                logging.INFO(traceback.format_exc())
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
                logging.INFO(traceback.format_exc())
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
        except Exception:
            logging.INFO(traceback.format_exc())
        return Response(data, status=status.HTTP_200_OK)


class CaseReport(generics.ListAPIView):
    serializer_class = ReportSerializer
    queryset = Report.objects.order_by('-test_time')[0:1]


# 根据用例运行时间搜索报告
class SearchReport(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = ReportDetail.objects.all()
    serializer_class = ReportDetailSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('test_time',)


# 根据用例运行时间搜索pass、fail用例数据
class SearchReports(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('test_time',)


# 获取10次最近的报告
class GetReports(generics.ListAPIView):
    queryset = Report.objects.order_by('-test_time')[0:10]
    serializer_class = ReportSerializer


# 获取报告的详细信息
class ReportDetails(generics.ListAPIView):
    # def get(self, request):
    # result = Report.objects.order_by('-test_time')[0:1].get().test_time
    # results = ReportDetail.objects.filter(test_time=result)
    # results_list = []
    # result_dict = {}
    # for item in results:
    #     result_dict['case_name'] = item.case_name
    #     result_dict['request_url'] = item.request_url
    #     result_dict['result'] = item.result
    #     results_list.append(result_dict)
    # print(results_list)
    # return Response(results_list)
    result_param = Report.objects.order_by('-test_time')[0:1].get().test_time
    queryset = ReportDetail.objects.filter(test_time=result_param)
    serializer_class = ReportDetailSerializer
