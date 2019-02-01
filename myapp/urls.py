# -*- coding:utf-8 -*-
from django.conf.urls import url
from django.contrib import admin
from myapp.views import InterfaceProject, InterfaceCase, UpdateProject, \
    UpdateCase, DeleteProject, DeleteCase, DeleteProjects, DeleteCases, \
    SearchProject, SearchCase, UserList, SearchUser, UpdateUser, DeleteUser, \
    DeleteUsers, ResetPwd, CaseReport, SearchReport, GetReports, ReportDetails, \
    SearchReports, SearchTask, TimingTasks, DeleteTask, DeleteTasks, \
    UpdateTaskStatus, CopyCase, Upload, UploadProject
from .runScripts import Register, RunCase, RunCases, TestCaseDoc
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework.schemas import get_schema_view
from rest_framework_swagger.renderers import SwaggerUIRenderer, OpenAPIRenderer
from rest_framework.documentation import include_docs_urls

schema_view = get_schema_view(title='Users API',
                              renderer_classes=[OpenAPIRenderer,
                                                SwaggerUIRenderer])

urlpatterns = [
    url(r'^api-auth/$', obtain_jwt_token, name='login'),
    url(r'^project_list/$', InterfaceProject.as_view(), name='project_list'),
    url(r'^create_project/$', InterfaceProject.as_view(),
        name='create_project'),
    url(r'^update_project/(?P<pk>\d+)$', UpdateProject.as_view(),
        name='update_project'),
    url(r'^delete_project/(?P<pk>\d+)$', DeleteProject.as_view(),
        name='delete_project'),
    url(r'^case_list/$', InterfaceCase.as_view(),
        name='case_list'),
    url(r'^create_case/$', InterfaceCase.as_view(),
        name='create_case'),
    url(r'^update_case/(?P<pk>\d+)$', UpdateCase.as_view(),
        name='update_case'),
    url(r'^delete_case/(?P<pk>\d+)$', DeleteCase.as_view(),
        name='delete_case'),
    url(r'^delete_projects/$', DeleteProjects.as_view(),
        name='delete_projects'),
    url(r'^delete_cases/$', DeleteCases.as_view(), name='delete_cases'),
    url(r'^search_project/$', SearchProject.as_view({'get': 'list'}),
        name='search_project'),
    url(r'^search_case/$', SearchCase.as_view({'get': 'list'}),
        name='search_case'),
    url(r'^register/$', Register.Register.as_view(), name='register'),
    url(r'^run/$', RunCase.RunCase.as_view(), name='run_case'),
    url(r'^user_list/$', UserList.as_view(), name='user_list'),
    url(r'^create_user/$', Register.Register.as_view(), name='user_list'),
    url(r'^search_user/$', SearchUser.as_view({'get': 'list'}),
        name='search_user'),
    url(r'^update_user/(?P<pk>\d+)$', UpdateUser.as_view(), name='update_user'),
    url(r'^delete_user/(?P<pk>\d+)$', DeleteUser.as_view(),
        name='delete_user'),
    url(r'^delete_users/$', DeleteUsers.as_view(),
        name='delete_users'),
    url(r'^reset_pwd/(?P<pk>\d+)$', ResetPwd.as_view(), name='reset_pwd'),
    url(r'^run_cases/$', RunCases.RunCases.as_view(), name='run_cases'),
    url(r'^make_cases/$', TestCaseDoc.MakeCases.as_view(), name='make_cases'),
    url(r'^case_report/$', CaseReport.as_view(), name='case_report'),
    url(r'^search_report/$', SearchReport.as_view({'get': 'list'}),
        name='search_report'),
    url(r'^get_detail_report/$', ReportDetails.as_view(),
        name='get_detail_report'),
    url(r'^get_report/$', GetReports.as_view(),
        name='get_report'),
    url(r'^search_reports/$', SearchReports.as_view({'get': 'list'}),
        name='search_reports'),
    url(r'^search_task/$', SearchTask.as_view({'get': 'list'}),
        name='search_task'),
    url(r'^add_task/$', TimingTasks.as_view(), name='add_task'),
    url(r'^get_task/$', TimingTasks.as_view(), name='get_task'),
    url(r'^delete_task/(?P<pk>\d+)$', DeleteTask.as_view(), name='delete_task'),
    url(r'^delete_tasks/$', DeleteTasks.as_view(), name='delete_tasks'),
    url(r'^stop_task/(?P<pk>\d+)$', UpdateTaskStatus.as_view(),
        name='stop_task'),
    url(r'^copy/$', CopyCase.as_view(), name='copy_case'),
    url(r'^upload/$', Upload.as_view(), name='upload'),
    url(r'^upload_project/$', UploadProject.as_view(), name='upload_project'),

    url('docs/', include_docs_urls(title=u'文档')),
]
