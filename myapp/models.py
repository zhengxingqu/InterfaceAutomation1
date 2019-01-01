# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import AbstractUser

from django.db import models


# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=100, default='', verbose_name='姓名',
                                unique=True)
    password = models.CharField(max_length=100, default='', verbose_name='密码')
    sex = models.CharField(max_length=10, default='', verbose_name='性别')
    iphone = models.CharField(max_length=30, verbose_name='手机号')
    head_portrait = models.ImageField(verbose_name='头像', default='')
    isdelete = models.CharField(default=True, max_length=10)

    def __unicode__(self):
        return self.username


class Project(models.Model):
    project_name = models.CharField(max_length=50, default='',
                                    verbose_name='项目名')
    permanent_address = models.CharField(max_length=100, default='',
                                         verbose_name='固定地址')
    isdelete = models.CharField(max_length=10, default=True, verbose_name='状态')
    request_header = models.CharField(max_length=100, default='',
                                      verbose_name='请求头')

    def __unicode__(self):
        return self.project_name


class Case(models.Model):
    case_name = models.CharField(max_length=100, default='',
                                 verbose_name='测试用例名称')
    project_name = models.ForeignKey(Project, max_length=100,
                                     verbose_name='项目名称',
                                     related_name='testcase_project',
                                     on_delete=models.CASCADE, default='')
    request_type = models.CharField(max_length=20, default='',
                                    verbose_name='接口请求类型')
    request_param = models.CharField(max_length=300, default='',
                                     verbose_name='接口请求参数')
    # request_header = models.CharField(max_length=100, default='',
    #                                   verbose_name='请求头')
    isdelete = models.CharField(max_length=10, default=True, verbose_name='状态')
    expected_result = models.CharField(max_length=300, default='',
                                       verbose_name='预期结果')
    login_way = models.CharField(max_length=50, default='',
                                 verbose_name='登陆方式')
    return_result = models.CharField(max_length=300, default='',
                                     verbose_name='接口运行返回结果')
    case_result = models.CharField(max_length=20, default='未开始',
                                   verbose_name='用例运行结果', )

    def __unicode__(self):
        return self.case_name
