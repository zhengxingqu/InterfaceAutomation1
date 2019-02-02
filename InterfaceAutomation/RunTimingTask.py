# -*- coding:utf-8 -*-
# import os, django
#
# os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

# django.setup()
from myapp.models import TimingTask, Case
from apscheduler.schedulers.blocking import BlockingScheduler
from myapp.runScripts.RunAllCases import RunCases
from myapp.runScripts.ReportEmail import ReportEmial

run_times = TimingTask.objects.filter(isdelete=True, is_stop=u'正常')
sched = BlockingScheduler()

rc = RunCases()
report = ReportEmial()


def test():
    try:
        rc.post()
        report.report()
    except Exception as e:
        print(e)
