# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2019-01-01 11:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_project_request_header'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='case',
            name='request_header',
        ),
    ]