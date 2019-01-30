#!/usr/bin/python
# -*- coding: UTF-8 -*-
from myapp.models import Report
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'InterfaceAutomation.settings'

class ReportEmial(object):
    def report(self):
        result_param = Report.objects.order_by('-test_time')[
                       0:1].get().test_time
        pass_number = Report.objects.order_by('-test_time')[
                      0:1].get().pass_number
        fail_number = Report.objects.order_by('-test_time')[
                      0:1].get().fail_number
        smtpserver = "smtp.qq.com"
        port = 465
        sender_man = "481105557@qq.com"
        receiver = "481105557@qq.com"
        psw = 'zcxyxujiyvhrcbci'

        subject = u'用例运行测试报告'
        body = u'运行时间为' + result_param + u'通过个数' + pass_number + u'失败个数' + fail_number
        msg = MIMEText(body, "html", "utf-8")
        msg['from'] = sender_man
        msg['to'] = receiver
        msg['subject'] = subject

        smtp = smtplib.SMTP_SSL(smtpserver, port)
        smtp.login(sender_man, psw)
        smtp.sendmail(sender_man, receiver, msg.as_string())
        smtp.quit()
