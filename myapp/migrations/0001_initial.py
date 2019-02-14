# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2019-01-12 09:39
from __future__ import unicode_literals

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('username', models.CharField(default='', max_length=100, unique=True, verbose_name='\u59d3\u540d')),
                ('password', models.CharField(default='', max_length=100, verbose_name='\u5bc6\u7801')),
                ('sex', models.CharField(default='', max_length=10, verbose_name='\u6027\u522b')),
                ('iphone', models.CharField(max_length=30, verbose_name='\u624b\u673a\u53f7')),
                ('head_portrait', models.ImageField(default='', upload_to=b'', verbose_name='\u5934\u50cf')),
                ('isdelete', models.CharField(default=True, max_length=10)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('case_name', models.CharField(default='', max_length=100, verbose_name='\u6d4b\u8bd5\u7528\u4f8b\u540d\u79f0')),
                ('request_type', models.CharField(default='', max_length=20, verbose_name='\u63a5\u53e3\u8bf7\u6c42\u7c7b\u578b')),
                ('request_param', models.CharField(blank=True, default='', max_length=300, verbose_name='\u63a5\u53e3\u8bf7\u6c42\u53c2\u6570')),
                ('isdelete', models.CharField(default=True, max_length=10, verbose_name='\u72b6\u6001')),
                ('expected_result', models.CharField(default='', max_length=300, verbose_name='\u9884\u671f\u7ed3\u679c')),
                ('return_result', models.TextField(default='', verbose_name='\u63a5\u53e3\u8fd0\u884c\u8fd4\u56de\u7ed3\u679c')),
                ('case_result', models.CharField(default='\u672a\u5f00\u59cb', max_length=20, verbose_name='\u7528\u4f8b\u8fd0\u884c\u7ed3\u679c')),
                ('url', models.CharField(default='', max_length=100, verbose_name='\u63a5\u53e3\u5730\u5740')),
                ('invoking_login', models.CharField(default='', max_length=10, verbose_name='\u8c03\u7528\u767b\u9646\u63a5\u53e3')),
                ('invoking_other_interface', models.CharField(default='', max_length=100, verbose_name='\u8c03\u7528\u5176\u4ed6\u63a5\u53e3\u4fe1\u606f')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(default='', max_length=50, verbose_name='\u9879\u76ee\u540d')),
                ('permanent_address', models.CharField(default='', max_length=100, verbose_name='\u56fa\u5b9a\u5730\u5740')),
                ('isdelete', models.CharField(default=True, max_length=10, verbose_name='\u72b6\u6001')),
                ('request_header', models.CharField(default='', max_length=100, verbose_name='\u8bf7\u6c42\u5934')),
                ('login_way', models.CharField(default='', max_length=100, verbose_name='\u767b\u9646\u65b9\u5f0f')),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pass_number', models.IntegerField(null=True, verbose_name='\u901a\u8fc7\u4e2a\u6570')),
                ('fail_number', models.IntegerField(null=True, verbose_name='\u5931\u8d25\u4e2a\u6570')),
                ('test_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='ReportDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('case_name', models.CharField(default='', max_length=100, null=True, verbose_name='\u62a5\u544a\u6d4b\u8bd5\u7528\u4f8b\u540d\u79f0')),
                ('request_url', models.CharField(default='', max_length=100, null=True, verbose_name='\u62a5\u544a\u8bf7\u6c42\u5730\u5740')),
                ('result', models.CharField(default='', max_length=50, null=True, verbose_name='\u7528\u4f8b\u6267\u884c\u72b6\u6001')),
                ('test_time', models.ManyToManyField(to='myapp.Report', verbose_name='\u7528\u4f8b\u6267\u884c\u65f6\u95f4')),
            ],
        ),
        migrations.AddField(
            model_name='case',
            name='project_name',
            field=models.ForeignKey(default='', max_length=100, on_delete=django.db.models.deletion.CASCADE, related_name='testcase_project', to='myapp.Project', verbose_name='\u9879\u76ee\u540d\u79f0'),
        ),
    ]
