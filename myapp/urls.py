from django.conf.urls import url
from django.contrib import admin
from myapp.views import InterfaceProject, InterfaceCase, UpdateProject, \
    UpdateCase, DeleteProject, DeleteCase, DeleteProjects, DeleteCases, \
    SearchProject, SearchCase
from .runScripts import Register, RunCase
from rest_framework_jwt.views import obtain_jwt_token

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
    url(r'^run/$', RunCase.RunCase.as_view(), name='run_case')

]
