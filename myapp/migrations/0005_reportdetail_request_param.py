# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2019-01-13 08:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20190113_0833'),
    ]

    operations = [
        migrations.AddField(
            model_name='reportdetail',
            name='request_param',
            field=models.CharField(default='', max_length=500, verbose_name='\u63a5\u53e3\u8bf7\u6c42\u53c2\u6570'),
        ),
    ]