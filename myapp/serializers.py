# -*- coding:utf-8 -*-
from rest_framework import serializers
from .models import User, Project, Case, Report, ReportDetail
from rest_framework.validators import UniqueValidator


class ProjectSerializer(serializers.ModelSerializer):
    project_name = serializers.CharField(max_length=50,
                                         validators=[UniqueValidator(
                                             queryset=Project.objects.filter(
                                                 isdelete=True),
                                             message=("项目名已存在"))],
                                         error_messages=({'blank':
                                                              '项目名称不能为空'}))
    permanent_address = serializers.CharField(max_length=100,
                                              validators=[UniqueValidator(
                                                  queryset=Project.objects.filter(
                                                      isdelete=True),
                                                  message=("固定IP已存在"))],
                                              error_messages=({'blank':
                                                                   '固定IP不能为空'}))
    isdelete = serializers.CharField(max_length=10, default=True,
                                     allow_blank=True)
    request_header = serializers.CharField(max_length=100, default='')
    login_way = serializers.CharField(max_length=100, default='')

    class Meta:
        model = Project
        fields = (
            'project_name', 'permanent_address', 'id', 'isdelete',
            'request_header', 'login_way')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class CaseSerializer(serializers.ModelSerializer):
    case_name = serializers.CharField(max_length=100,
                                      validators=[UniqueValidator(
                                          queryset=Case.objects.filter(
                                              isdelete=True),
                                          message=("已存在相同名称测试用例"))],
                                      error_messages=({'blank':
                                                           '测试用例名称不能为空'}))
    project_name = serializers.SlugRelatedField(slug_field="project_name",
                                                queryset=Project.objects.filter(
                                                    isdelete=True))
    request_type = serializers.CharField(max_length=20)
    request_param = serializers.CharField(max_length=300, allow_blank=True,
                                          required=False)
    # request_header = serializers.CharField(max_length=100)
    isdelete = serializers.CharField(max_length=10, allow_blank=True,
                                     default=True)
    expected_result = serializers.CharField(max_length=300)
    return_result = serializers.CharField(allow_blank=True,
                                          required=False)
    # login_way = serializers.CharField(max_length=50)
    case_result = serializers.CharField(max_length=20, allow_blank=True,
                                        required=False)
    url = serializers.CharField(max_length=100, default='')
    invoking_login = serializers.CharField(max_length=10, default='',
                                           allow_blank=True)
    invoking_other_interface = serializers.CharField(max_length=100, default='',
                                                     allow_blank=True)

    class Meta:
        model = Case
        fields = (
            'case_name', 'request_type', 'request_param',
            'isdelete', 'expected_result', 'return_result',
            'case_result', 'id', 'project_name', 'url', 'invoking_login',
            'invoking_other_interface')


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = '__all__'


class ReportDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportDetail
        fields = '__all__'
