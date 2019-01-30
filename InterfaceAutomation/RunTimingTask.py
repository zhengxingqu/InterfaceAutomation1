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
    # print('********')
    # t1()
    try:
        rc.post()
        report.report()
    except Exception as e:
        print(e)
    # print('******************')
    # t1()
    # print('********')
    # a = 1
    # b = 2
    # print(a + b)
    # RunCases.post()
    # for time in run_times:
    #     try:
    #         print(time)
    #     except Exception as e:
    #         print(e)
    #     # print(time.time)
    #     # print('*********')
    #     try:
    #         sched.add_job(test1, 'date', run_date=time.time)
    #         sched.start()
    #     except Exception as e:
    #         print('********')
    #         print(e)
    #
    # try:
    #     sched.start()
    # except Exception as e:
    #     print(e)

#
#
# #
# if __name__ == "__main__":
#     test()
# # def test():
# #     print('************')


# from apscheduler.schedulers.blocking import BlockingScheduler
# import datetime
#
#
# def my_job1():
#     print(
#         'my_job1 is running, Now is %s' % datetime.datetime.now().strftime(
#             "%Y-%m-%d %H:%M:%S"))
#
#
# def my_job2():
#     print(
#         'my_job2 is running, Now is %s' % datetime.datetime.now().strftime(
#             "%Y-%m-%d %H:%M:%S"))
#
#
# sched = BlockingScheduler()
# # 每隔5秒运行一次my_job1
# sched.add_job(my_job1, 'interval', seconds=5, id='my_job1')
# # 每隔5秒运行一次my_job2
# sched.add_job(my_job2, 'cron', second='*/5', id='my_job2')
# sched.start()
