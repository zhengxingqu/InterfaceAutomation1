from apscheduler.schedulers.blocking import BlockingScheduler
import datetime


def my_job1():
    print(
        'my_job1 is running, Now is %s' % datetime.datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"))


def my_job2():
    print(
        'my_job2 is running, Now is %s' % datetime.datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"))


sched = BlockingScheduler()
# 每隔5秒运行一次my_job1
sched.add_job(my_job1, 'interval', seconds=5, id='my_job1')
# 每隔5秒运行一次my_job2
sched.add_job(my_job2, 'cron', second='*/5', id='my_job2')
sched.start()
