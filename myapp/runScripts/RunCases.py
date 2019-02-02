# -*- coding:utf-8 -*-
from rest_framework.views import APIView
from ..models import Case, Project, Report, ReportDetail
import logging
import requests
from rest_framework.response import Response
import re
import datetime
import logging
import traceback

logging.basicConfig(filename='runcases.log', level=logging.INFO)


class RunCases(APIView):
    # 登陆接口返回数据

    pass_number = 0
    fail_number = 0

    def login(self):
        try:
            login_request_param = Case.objects.get(isdelete=True,
                                                   id=invoking_login).request_param
            login_url = Case.objects.get(isdelete=True, id=invoking_login).url
            login_permanent_address = Project.objects.get(isdelete=True,
                                                          project_name=Case.objects.get(
                                                              isdelete=True,
                                                              id=invoking_login).project_name).permanent_address
            login_request_url = login_permanent_address + login_url
            login_request_header = Project.objects.get(isdelete=True,
                                                       project_name=Case.objects.get(
                                                           isdelete=True,
                                                           id=invoking_login).project_name).request_header
            # login_login_way = Project.objects.get(isdelete=True,
            #                                       id=invoking_login).login_way

            result = requests.post(login_request_url,
                                   json=eval(login_request_param),
                                   headers=eval(login_request_header),
                                   verify=False)
        except Exception:
            logging.INFO(traceback.format_exc())
        # if login_login_way == 'cookies':
        #     return result.cookies
        # else:
        #     jwt = 'JWT ' + result.json()['token']
        #     return jwt
        return result

    # 不调用登陆、其他接口返回数据

    def get_no_login_case(self):
        try:
            result = requests.get(request_url, params=eval(request_param),
                                  headers=eval(request_header), verify=False)
            if expected_result.encode('utf-8') in result.content:
                Case.objects.filter(id=int(number_id)).update(
                    case_result='成功')
                Case.objects.filter(id=int(number_id)).update(
                    return_result=result.json())
                RunCases.pass_number += 1

                try:
                    ReportDetail.objects.create(case_name=case_name,
                                                request_url=request_url,
                                                result='PASS',
                                                test_time=test_time,
                                                request_type=request_type,
                                                case_result=result.json(),
                                                request_param=request_param)
                except Exception:
                    logging.INFO(traceback.format_exc())
            else:
                Case.objects.filter(id=int(number_id)).update(
                    case_result='失败')
                RunCases.fail_number += 1
                try:
                    ReportDetail.objects.create(case_name=case_name,
                                                request_url=request_url,
                                                result='FAIL',
                                                test_time=test_time,
                                                request_type=request_type,
                                                case_result=result.json(),
                                                request_param=request_param)
                except Exception:
                    logging.INFO(traceback.format_exc())
        except Exception:
            logging.INFO(traceback.format_exc())

    def post_no_login_case(self):
        try:
            result = requests.post(request_url, json=eval(request_param),
                                   headers=eval(request_header), verify=False)
            if expected_result.encode('utf-8') in result.content:
                Case.objects.filter(id=int(number_id)).update(
                    case_result='成功')
                Case.objects.filter(id=int(number_id)).update(
                    return_result=result.json())
                RunCases.pass_number += 1
                try:
                    ReportDetail.objects.create(case_name=case_name,
                                                request_url=request_url,
                                                result='PASS',
                                                test_time=test_time,
                                                request_type=request_type,
                                                case_result=result.json(),
                                                request_param=request_param)
                except Exception:
                    logging.INFO(traceback.format_exc())
            else:
                Case.objects.filter(id=int(number_id)).update(
                    case_result='失败')
                RunCases.fail_number += 1
                try:
                    ReportDetail.objects.create(case_name=case_name,
                                                request_url=request_url,
                                                result='FAIL',
                                                test_time=test_time,
                                                request_type=request_type,
                                                case_result=result.json(),
                                                request_param=request_param)
                except Exception:
                    logging.INFO(traceback.format_exc())
        except Exception:
            logging.INFO(traceback.format_exc())

    def put_no_login_case(self):
        try:
            result = requests.put(request_url, json=eval(request_param),
                                  headers=eval(request_header), verify=False)
            if expected_result.encode('utf-8') in result.content:
                Case.objects.filter(id=int(number_id)).update(
                    case_result='成功')
                Case.objects.filter(id=int(number_id)).update(
                    return_result=result.json())
                RunCases.pass_number += 1
                try:
                    ReportDetail.objects.create(case_name=case_name,
                                                request_url=request_url,
                                                result='PASS',
                                                test_time=test_time,
                                                request_type=request_type,
                                                case_result=result.json(),
                                                request_param=request_param)
                except Exception:
                    logging.INFO(traceback.format_exc())
            else:
                Case.objects.filter(id=int(number_id)).update(
                    case_result='失败')
                RunCases.fail_number += 1
                try:
                    ReportDetail.objects.create(case_name=case_name,
                                                request_url=request_url,
                                                result='FAIL',
                                                test_time=test_time,
                                                request_type=request_type,
                                                case_result=result.json(),
                                                request_param=request_param)
                except Exception:
                    logging.INFO(traceback.format_exc())
        except Exception:
            logging.INFO(traceback.format_exc())

    def delete_no_login_case(self):
        try:
            result = requests.delete(request_url, json=eval(request_param),
                                     headers=eval(request_header), verify=False)
            if expected_result.encode('utf-8') in result.content:
                Case.objects.filter(id=int(number_id)).update(
                    case_result='成功')
                Case.objects.filter(id=int(number_id)).update(
                    return_result=result.json())
                RunCases.pass_number += 1
                try:
                    ReportDetail.objects.create(case_name=case_name,
                                                request_url=request_url,
                                                result='PASS',
                                                test_time=test_time,
                                                request_type=request_type,
                                                case_result=result.json(),
                                                request_param=request_param)
                except Exception:
                    logging.INFO(traceback.format_exc())
            else:
                Case.objects.filter(id=int(number_id)).update(
                    case_result='失败')
                RunCases.fail_number += 1
                try:
                    ReportDetail.objects.create(case_name=case_name,
                                                request_url=request_url,
                                                result='FAIL',
                                                test_time=test_time,
                                                request_type=request_type,
                                                case_result=result.json(),
                                                request_param=request_param)
                except Exception:
                    logging.INFO(traceback.format_exc())
        except Exception:
            logging.INFO(traceback.format_exc())

    # 无需登陆、调用其他接口数据
    def get_nologin_invoking_interface(self):
        for interface_id in eval(invoking_other_interface):
            try:

                interface_id_str = '[' + interface_id + ']'
                id_res = re.compile('(\[\d\])')
                res_result = id_res.findall(request_param)
                # 遍历正则匹配请求参数后的列表
                for i in res_result:
                    # 请求参数中对应不同的请求接口
                    if interface_id_str == i:
                        return_result = Case.objects.get(id=interface_id,
                                                         isdelete=True).return_result
                        replace_id = re.compile('(id: )(\d)?')
                        return_id = replace_id.search(return_result)
                        new_request_param = request_param.replace(i,
                                                                  return_id.group(
                                                                      2))
                        result = requests.get(request_url,
                                              params=eval(new_request_param),
                                              headers=eval(request_header),
                                              verify=False)
                        if expected_result.encode('utf-8') in result.content:
                            Case.objects.filter(
                                id=int(number_id)).update(
                                case_result='成功')
                            Case.objects.filter(
                                id=int(number_id)).update(
                                return_result=result.json())
                            RunCases.pass_number += 1
                            try:
                                ReportDetail.objects.create(case_name=case_name,
                                                            request_url=request_url,
                                                            result='PASS',
                                                            test_time=test_time,
                                                            request_type=request_type,
                                                            case_result=result.json(),
                                                            request_param=request_param)
                            except Exception:
                                logging.INFO(traceback.format_exc())
                        else:
                            Case.objects.filter(
                                id=int(number_id)).update(
                                case_result='失败')
                            RunCases.fail_number += 1
                            try:
                                ReportDetail.objects.create(case_name=case_name,
                                                            request_url=request_url,
                                                            result='FAIL',
                                                            test_time=test_time,
                                                            request_type=request_type,
                                                            case_result=result.json(),
                                                            request_param=request_param)
                            except Exception:
                                logging.INFO(traceback.format_exc())
            except Exception:
                logging.INFO(traceback.format_exc())

    def post_nologin_invoking_interface(self):
        for interface_id in eval(invoking_other_interface):
            try:

                interface_id_str = '[' + interface_id + ']'
                id_res = re.compile('(\[\d\])')
                res_result = id_res.findall(request_param)
                # 遍历正则匹配请求参数后的列表
                for i in res_result:
                    # 请求参数中对应不同的请求接口
                    if interface_id_str == i:
                        return_result = Case.objects.get(id=interface_id,
                                                         isdelete=True).return_result
                        replace_id = re.compile('(id: )(\d)?')
                        return_id = replace_id.search(return_result)
                        new_request_param = request_param.replace(i,
                                                                  return_id.group(
                                                                      2))
                        result = requests.post(request_url,
                                               json=eval(new_request_param),
                                               headers=eval(request_header),
                                               verify=False)
                        if expected_result.encode('utf-8') in result.content:
                            Case.objects.filter(
                                id=int(number_id)).update(
                                case_result='成功')
                            Case.objects.filter(
                                id=int(number_id)).update(
                                return_result=result.json())
                            RunCases.pass_number += 1
                            try:
                                ReportDetail.objects.create(case_name=case_name,
                                                            request_url=request_url,
                                                            result='PASS',
                                                            test_time=test_time,
                                                            request_type=request_type,
                                                            case_result=result.json(),
                                                            request_param=request_param)
                            except Exception:
                                logging.INFO(traceback.format_exc())
                        else:
                            Case.objects.filter(
                                id=int(number_id)).update(
                                case_result='失败')
                            RunCases.fail_number += 1
                            try:
                                ReportDetail.objects.create(case_name=case_name,
                                                            request_url=request_url,
                                                            result='FAIL',
                                                            test_time=test_time,
                                                            request_type=request_type,
                                                            case_result=result.json(),
                                                            request_param=request_param)
                            except Exception:
                                logging.INFO(traceback.format_exc())
            except Exception:
                logging.INFO(traceback.format_exc())

    def put_nologin_invoking_interface(self):
        for interface_id in eval(invoking_other_interface):
            try:

                interface_id_str = '[' + interface_id + ']'
                id_res = re.compile('(\[\d\])')
                res_result = id_res.findall(request_param)
                # 遍历正则匹配请求参数后的列表
                for i in res_result:
                    # 请求参数中对应不同的请求接口
                    if interface_id_str == i:
                        return_result = Case.objects.get(id=interface_id,
                                                         isdelete=True).return_result
                        replace_id = re.compile('(id: )(\d)?')
                        return_id = replace_id.search(return_result)
                        new_request_param = request_param.replace(i,
                                                                  return_id.group(
                                                                      2))
                        result = requests.put(request_url,
                                              json=eval(new_request_param),
                                              headers=eval(request_header),
                                              verify=False)
                        if expected_result.encode('utf-8') in result.content:
                            Case.objects.filter(
                                id=int(number_id)).update(
                                case_result='成功')
                            Case.objects.filter(
                                id=int(number_id)).update(
                                return_result=result.json())
                            RunCases.pass_number += 1
                            try:
                                ReportDetail.objects.create(case_name=case_name,
                                                            request_url=request_url,
                                                            result='PASS',
                                                            test_time=test_time,
                                                            request_type=request_type,
                                                            case_result=result.json(),
                                                            request_param=request_param)
                            except Exception:
                                logging.INFO(traceback.format_exc())
                        else:
                            Case.objects.filter(
                                id=int(number_id)).update(
                                case_result='失败')
                            RunCases.fail_number += 1
                            try:
                                ReportDetail.objects.create(case_name=case_name,
                                                            request_url=request_url,
                                                            result='FAIL',
                                                            test_time=test_time,
                                                            request_type=request_type,
                                                            case_result=result.json(),
                                                            request_param=request_param)
                            except Exception:
                                logging.INFO(traceback.format_exc())
            except Exception as e:
                logging.debug(e)

    def delete_nologin_invoking_interface(self):
        new_request_param = ''
        new_request_url = ''
        for index, interface_id in enumerate(eval(invoking_other_interface)):
            try:
                interface_id_str = '[' + str(index + 1) + ']'
                id_res = re.compile('(\[\d\])')
                res_result = id_res.findall(request_param)
                res_url = id_res.findall(request_url)
                # 遍历正则匹配请求参数后的列表
                if len(res_result) > 0:
                    for i in res_result:
                        # 请求参数中对应不同的请求接口
                        if interface_id_str == i:
                            return_result = Case.objects.get(id=interface_id,
                                                             isdelete=True).return_result
                            replace_id = re.compile("(\'id\': )(\d)?")
                            return_id = replace_id.search(return_result)
                            new_request_param = request_param.replace(i,
                                                                      return_id.group(
                                                                          2))
                for i in res_url:
                    # 请求参数中对应不同的请求接口
                    if interface_id_str == i:
                        return_result = Case.objects.get(
                            id=interface_id,
                            isdelete=True).return_result
                        replace_id = re.compile("(\'id\': )(\d)?")
                        return_id = replace_id.search(return_result)
                        new_request_url = request_url.replace(i,
                                                              return_id.group(
                                                                  2))

            except Exception:
                logging.INFO(traceback.format_exc())
        if new_request_param == '':
            new_request_param = request_param
        if new_request_url == '':
            new_request_param = request_url

        try:
            result = requests.delete(new_request_url,
                                     json=eval(new_request_param),
                                     headers=eval(request_header),
                                     verify=False)
            if expected_result.encode(
                    'utf-8') in result.content:
                Case.objects.filter(
                    id=int(number_id)).update(
                    case_result='成功')
                Case.objects.filter(
                    id=int(number_id)).update(
                    return_result=result.json())
                RunCases.pass_number += 1
                try:
                    ReportDetail.objects.create(case_name=case_name,
                                                request_url=request_url,
                                                result='PASS',
                                                test_time=test_time,
                                                request_type=request_type,
                                                case_result=result.json(),
                                                request_param=request_param)
                except Exception:
                    logging.INFO(traceback.format_exc())
            else:
                Case.objects.filter(
                    id=int(number_id)).update(
                    case_result='失败')
                RunCases.fail_number += 1
                try:
                    ReportDetail.objects.create(case_name=case_name,
                                                request_url=request_url,
                                                result='FAIL',
                                                test_time=test_time,
                                                request_type=request_type,
                                                case_result=result.json(),
                                                request_param=request_param)
                except Exception:
                    logging.INFO(traceback.format_exc())
        except Exception:
            logging.INFO(traceback.format_exc())

    # def get_login_invoking_interface(self):
    #     for interface_id in eval(invoking_other_interface):
    #         try:
    #             interface_id_str = '[' + interface_id + ']'
    #             id_res = re.compile('(\[\d\])')
    #             res_result = id_res.findall(request_param)
    #             # 遍历正则匹配请求参数后的列表
    #             for i in res_result:
    #                 # 请求参数中对应不同的请求接口
    #                 if interface_id_str == i:
    #                     return_result = Case.objects.get(id=interface_id,
    #                                                      isdelete=True).return_result
    #                     replace_id = re.compile('(id: )(\d)?')
    #                     return_id = replace_id.search(return_result)
    #                     new_request_param = request_param.replace(i,
    #                                                               return_id.group(
    #                                                                   2))
    #                     result = requests.get(request_url,
    #                                           params=eval(new_request_param),
    #                                           headers=eval(request_header),
    #                                           verify=False)
    #                     if expected_result.encode('utf-8') in result.content:
    #                         Case.objects.filter(
    #                             id=int(number_id['suite_id'])).update(
    #                             case_result='成功')
    #                         Case.objects.filter(
    #                             id=int(number_id['suite_id'])).update(
    #                             return_result=result.json())
    #                     else:
    #                         Case.objects.filter(
    #                             id=int(number_id['suite_id'])).update(
    #                             case_result='失败')
    #         except Exception as e:
    #             logging.debug(e)

    # 调用登陆、不调用其他接口
    def get_login_no_invoking_interface(self):

        if login_way == 'cookies':
            cookie = self.login().cookies
            try:
                result = requests.get(request_url, params=eval(request_param),
                                      headers=eval(request_header),
                                      verify=False,
                                      cookies=cookie)
                if expected_result.encode('utf-8') in result.content:
                    Case.objects.filter(id=int(number_id)).update(
                        case_result='成功')
                    Case.objects.filter(id=int(number_id)).update(
                        return_result=result.json())
                    RunCases.pass_number += 1
                    try:
                        ReportDetail.objects.create(case_name=case_name,
                                                    request_url=request_url,
                                                    result='PASS',
                                                    test_time=test_time,
                                                    request_type=request_type,
                                                    case_result=result.json(),
                                                    request_param=request_param)
                    except Exception:
                        logging.INFO(traceback.format_exc())
                else:
                    Case.objects.filter(id=int(number_id)).update(
                        case_result='失败')
                    RunCases.fail_number += 1
                    try:
                        ReportDetail.objects.create(case_name=case_name,
                                                    request_url=request_url,
                                                    result='FAIL',
                                                    test_time=test_time,
                                                    request_type=request_type,
                                                    case_result=result.json(),
                                                    request_param=request_param)
                    except Exception:
                        logging.INFO(traceback.format_exc())
            except Exception as e:
                return e
        else:
            jwt = 'JWT ' + self.login().json()['token']
            request_header['Authorization'] = jwt
            try:
                result = requests.get(request_url, params=eval(request_param),
                                      headers=eval(request_header),
                                      verify=False)
                if expected_result.encode('utf-8') in result.content:
                    Case.objects.filter(id=int(number_id)).update(
                        case_result='成功')
                    Case.objects.filter(id=int(number_id)).update(
                        return_result=result.json())
                    RunCases.pass_number += 1
                    try:
                        ReportDetail.objects.create(case_name=case_name,
                                                    request_url=request_url,
                                                    result='PASS',
                                                    test_time=test_time,
                                                    request_type=request_type,
                                                    case_result=result.json(),
                                                    request_param=request_param)
                    except Exception:
                        logging.INFO(traceback.format_exc())
                else:
                    Case.objects.filter(id=int(number_id)).update(
                        case_result='失败')
                    RunCases.fail_number += 1
                    try:
                        ReportDetail.objects.create(case_name=case_name,
                                                    request_url=request_url,
                                                    result='FAIL',
                                                    test_time=test_time,
                                                    request_type=request_type,
                                                    case_result=result.json(),
                                                    request_param=request_param)
                    except Exception:
                        logging.INFO(traceback.format_exc())
            except Exception:
                logging.INFO(traceback.format_exc())

    def post_login_no_invoking_interface(self):

        if login_way == 'cookies':
            cookie = self.login().cookies
            try:
                result = requests.post(request_url, json=eval(request_param),
                                       headers=eval(request_header),
                                       verify=False,
                                       cookies=cookie)
                if expected_result.encode('utf-8') in result.content:
                    Case.objects.filter(id=int(number_id)).update(
                        case_result='成功')
                    Case.objects.filter(id=int(number_id)).update(
                        return_result=result.json())
                    RunCases.pass_number += 1
                    try:
                        ReportDetail.objects.create(case_name=case_name,
                                                    request_url=request_url,
                                                    result='PASS',
                                                    test_time=test_time,
                                                    request_type=request_type,
                                                    case_result=result.json(),
                                                    request_param=request_param)
                    except Exception:
                        logging.INFO(traceback.format_exc())
                else:
                    Case.objects.filter(id=int(number_id)).update(
                        case_result='失败')
                    RunCases.fail_number += 1
                    try:
                        ReportDetail.objects.create(case_name=case_name,
                                                    request_url=request_url,
                                                    result='FAIL',
                                                    test_time=test_time,
                                                    request_type=request_type,
                                                    case_result=result.json(),
                                                    request_param=request_param)
                    except Exception:
                        logging.INFO(traceback.format_exc())
            except Exception:
                logging.INFO(traceback.format_exc())
        else:
            jwt = 'JWT ' + self.login().json()['token']
            request_header['Authorization'] = jwt
            try:
                result = requests.post(request_url, json=eval(request_param),
                                       headers=eval(request_header),
                                       verify=False)
                if expected_result.encode('utf-8') in result.content:
                    Case.objects.filter(id=int(number_id)).update(
                        case_result='成功')
                    Case.objects.filter(id=int(number_id)).update(
                        return_result=result.json())
                    RunCases.pass_number += 1
                    try:
                        ReportDetail.objects.create(case_name=case_name,
                                                    request_url=request_url,
                                                    result='PASS',
                                                    test_time=test_time,
                                                    request_type=request_type,
                                                    case_result=result.json(),
                                                    request_param=request_param)
                    except Exception:
                        logging.INFO(traceback.format_exc())
                else:
                    Case.objects.filter(id=int(number_id)).update(
                        case_result='失败')
                    RunCases.fail_number += 1
                    try:
                        ReportDetail.objects.create(case_name=case_name,
                                                    request_url=request_url,
                                                    result='FAIL',
                                                    test_time=test_time,
                                                    request_type=request_type,
                                                    case_result=result.json(),
                                                    request_param=request_param)
                    except Exception:
                        logging.INFO(traceback.format_exc())
            except Exception:
                logging.INFO(traceback.format_exc())

    def put_login_no_invoking_interface(self):

        if login_way == 'cookies':
            cookie = self.login().cookies
            try:
                result = requests.put(request_url, json=eval(request_param),
                                      headers=eval(request_header),
                                      verify=False,
                                      cookies=cookie)
                if expected_result.encode('utf-8') in result.content:
                    Case.objects.filter(id=int(number_id)).update(
                        case_result='成功')
                    Case.objects.filter(id=int(number_id)).update(
                        return_result=result.json())
                    RunCases.pass_number += 1
                    try:
                        ReportDetail.objects.create(case_name=case_name,
                                                    request_url=request_url,
                                                    result='PASS',
                                                    test_time=test_time,
                                                    request_type=request_type,
                                                    case_result=result.json(),
                                                    request_param=request_param)
                    except Exception:
                        logging.INFO(traceback.format_exc())
                else:
                    Case.objects.filter(id=int(number_id)).update(
                        case_result='失败')
                    RunCases.fail_number += 1
                    try:
                        ReportDetail.objects.create(case_name=case_name,
                                                    request_url=request_url,
                                                    result='FAIL',
                                                    test_time=test_time,
                                                    request_type=request_type,
                                                    case_result=result.json(),
                                                    request_param=request_param)
                    except Exception:
                        logging.INFO(traceback.format_exc())
            except Exception:
                logging.INFO(traceback.format_exc())
        else:
            jwt = 'JWT ' + self.login().json()['token']
            request_header['Authorization'] = jwt
            try:
                result = requests.put(request_url, json=eval(request_param),
                                      headers=eval(request_header),
                                      verify=False)
                if expected_result.encode('utf-8') in result.content:
                    Case.objects.filter(id=int(number_id)).update(
                        case_result='成功')
                    Case.objects.filter(id=int(number_id)).update(
                        return_result=result.json())
                    RunCases.pass_number += 1
                    try:
                        ReportDetail.objects.create(case_name=case_name,
                                                    request_url=request_url,
                                                    result='PASS',
                                                    test_time=test_time,
                                                    request_type=request_type,
                                                    case_result=result.json(),
                                                    request_param=request_param)
                    except Exception:
                        logging.INFO(traceback.format_exc())
                else:
                    Case.objects.filter(id=int(number_id)).update(
                        case_result='失败')
                    RunCases.fail_number += 1
                    try:
                        ReportDetail.objects.create(case_name=case_name,
                                                    request_url=request_url,
                                                    result='FAIL',
                                                    test_time=test_time,
                                                    request_type=request_type,
                                                    case_result=result.json(),
                                                    request_param=request_param).save()
                    except Exception:
                        logging.INFO(traceback.format_exc())
            except Exception:
                logging.INFO(traceback.format_exc())

    def delete_login_no_invoking_interface(self):

        if login_way == 'cookies':
            cookie = self.login().cookies
            try:
                result = requests.delete(request_url, json=eval(request_param),
                                         headers=eval(request_header),
                                         verify=False,
                                         cookies=cookie)
                if expected_result.encode('utf-8') in result.content:
                    Case.objects.filter(id=int(number_id)).update(
                        case_result='成功')
                    Case.objects.filter(id=int(number_id)).update(
                        return_result=result.json())
                    RunCases.pass_number += 1
                    try:
                        ReportDetail.objects.create(case_name=case_name,
                                                    request_url=request_url,
                                                    result='PASS',
                                                    test_time=test_time,
                                                    request_type=request_type,
                                                    case_result=result.json(),
                                                    request_param=request_param)
                    except Exception:
                        logging.INFO(traceback.format_exc())
                else:
                    Case.objects.filter(id=int(number_id)).update(
                        case_result='失败')
                    RunCases.fail_number += 1
                    try:
                        ReportDetail.objects.create(case_name=case_name,
                                                    request_url=request_url,
                                                    result='FAIL',
                                                    test_time=test_time,
                                                    request_type=request_type,
                                                    case_result=result.json(),
                                                    request_param=request_param)
                    except Exception:
                        logging.INFO(traceback.format_exc())
            except Exception:
                logging.INFO(traceback.format_exc())
        else:
            jwt = 'JWT ' + self.login().json()['token']
            request_header['Authorization'] = jwt
            try:
                result = requests.delete(request_url, json=eval(request_param),
                                         headers=eval(request_header),
                                         verify=False)
                if expected_result.encode('utf-8') in result.content:
                    Case.objects.filter(id=int(number_id)).update(
                        case_result='成功')
                    Case.objects.filter(id=int(number_id)).update(
                        return_result=result.json())
                    RunCases.pass_number += 1
                    try:
                        ReportDetail.objects.create(case_name=case_name,
                                                    request_url=request_url,
                                                    result='PASS',
                                                    test_time=test_time,
                                                    request_type=request_type,
                                                    case_result=result.json(),
                                                    request_param=request_param)
                    except Exception:
                        logging.INFO(traceback.format_exc())
                else:
                    Case.objects.filter(id=int(number_id)).update(
                        case_result='失败')
                    RunCases.fail_number += 1
                    try:
                        ReportDetail.objects.create(case_name=case_name,
                                                    request_url=request_url,
                                                    result='FAIL',
                                                    test_time=test_time,
                                                    request_type=request_type,
                                                    case_result=result.json(),
                                                    request_param=request_param)
                    except Exception:
                        logging.INFO(traceback.format_exc())
            except Exception:
                logging.INFO(traceback.format_exc())

    # 调用登陆及其他接口返回数据
    # 需要调用接口返回参数时，以【1】、【2】来对应需要调用的接口列表序号
    def get_login_invoking_interface(self):
        new_request_param = ''
        new_request_url = ''
        for index, interface_id in enumerate(eval(invoking_other_interface)):
            try:
                interface_id_str = '[' + str(index + 1) + ']'
                id_res = re.compile('(\[\d\])')
                res_result = id_res.findall(request_param)
                res_url = id_res.findall(request_url)
                # 遍历正则匹配请求参数后的列表
                if len(res_result) > 0:
                    for i in res_result:
                        # 请求参数中对应不同的请求接口
                        if interface_id_str == i:
                            return_result = Case.objects.get(id=interface_id,
                                                             isdelete=True).return_result
                            replace_id = re.compile("(\'id\': )(\d)?")
                            return_id = replace_id.search(return_result)
                            new_request_param = request_param.replace(i,
                                                                      return_id.group(
                                                                          2))
                for i in res_url:
                    # 请求参数中对应不同的请求接口
                    if interface_id_str == i:
                        return_result = Case.objects.get(
                            id=interface_id,
                            isdelete=True).return_result
                        replace_id = re.compile("(\'id\': )(\d)?")
                        return_id = replace_id.search(return_result)
                        new_request_url = request_url.replace(i,
                                                              return_id.group(
                                                                  2))

            except Exception:
                logging.INFO(traceback.format_exc())

        if new_request_param == '':
            new_request_param = request_param

        if new_request_url == '':
            new_request_param = request_url

        if login_way == 'cookies':
            cookie = self.login().cookies
            try:
                result = requests.get(new_request_url,
                                      params=eval(new_request_param),
                                      headers=eval(request_header),
                                      verify=False,
                                      cookies=cookie)
                if expected_result.encode(
                        'utf-8') in result.content:
                    Case.objects.filter(
                        id=int(number_id)).update(
                        case_result='成功')
                    Case.objects.filter(
                        id=int(number_id)).update(
                        return_result=result.json())
                    RunCases.pass_number += 1
                    try:
                        ReportDetail.objects.create(case_name=case_name,
                                                    request_url=request_url,
                                                    result='PASS',
                                                    test_time=test_time,
                                                    request_type=request_type,
                                                    case_result=result.json(),
                                                    request_param=request_param)
                    except Exception:
                        logging.INFO(traceback.format_exc())
                else:
                    Case.objects.filter(
                        id=int(number_id)).update(
                        case_result='失败')
                    RunCases.fail_number += 1
                    try:
                        ReportDetail.objects.create(case_name=case_name,
                                                    request_url=request_url,
                                                    result='FAIL',
                                                    test_time=test_time,
                                                    request_type=request_type,
                                                    case_result=result.json(),
                                                    request_param=request_param)
                    except Exception:
                        logging.INFO(traceback.format_exc())
            except Exception:
                logging.INFO(traceback.format_exc())

        else:
            jwt = 'JWT ' + self.login().json()['token']
            request_header['Authorization'] = jwt
            try:
                result = requests.get(new_request_url,
                                      params=eval(new_request_param),
                                      headers=eval(request_header),
                                      verify=False)
                if expected_result.encode(
                        'utf-8') in result.content:
                    Case.objects.filter(
                        id=int(number_id)).update(
                        case_result='成功')
                    Case.objects.filter(
                        id=int(number_id)).update(
                        return_result=result.json())
                    RunCases.pass_number += 1
                    try:
                        ReportDetail.objects.create(case_name=case_name,
                                                    request_url=request_url,
                                                    result='PASS',
                                                    test_time=test_time,
                                                    request_type=request_type,
                                                    case_result=result.json(),
                                                    request_param=request_param)
                    except Exception:
                        logging.INFO(traceback.format_exc())
                else:
                    Case.objects.filter(
                        id=int(number_id)).update(
                        case_result='失败')
                    RunCases.fail_number += 1
                    try:
                        ReportDetail.objects.create(case_name=case_name,
                                                    request_url=request_url,
                                                    result='FAIL',
                                                    test_time=test_time,
                                                    request_type=request_type,
                                                    case_result=result.json(),
                                                    request_param=request_param)
                    except Exception:
                        logging.INFO(traceback.format_exc())
            except Exception:
                logging.INFO(traceback.format_exc())

    def put_login_invoking_interface(self):

        new_request_param = ''
        new_request_url = ''

        for index, interface_id in enumerate(eval(invoking_other_interface)):
            try:
                interface_id_str = '[' + str(index + 1) + ']'
                id_res = re.compile('(\[\d\])')
                res_result = id_res.findall(request_param)
                res_url = id_res.findall(request_url)
                # 遍历正则匹配请求参数后的列表
                if len(res_result) > 0:
                    for i in res_result:
                        # 请求参数中对应不同的请求接口
                        if interface_id_str == i:
                            return_result = Case.objects.get(id=interface_id,
                                                             isdelete=True).return_result
                            replace_id = re.compile("(\'id\': )(\d)?")
                            return_id = replace_id.search(return_result)
                            new_request_param = request_param.replace(i,
                                                                      return_id.group(
                                                                          2))
                for i in res_url:
                    # 请求参数中对应不同的请求接口
                    if interface_id_str == i:
                        return_result = Case.objects.get(
                            id=interface_id,
                            isdelete=True).return_result
                        replace_id = re.compile("(\'id\': )(\d)?")
                        return_id = replace_id.search(return_result)
                        new_request_url = request_url.replace(i,
                                                              return_id.group(
                                                                  2))

            except Exception:
                logging.INFO(traceback.format_exc())

        if new_request_param == '':
            new_request_param = request_param
        if new_request_url == '':
            new_request_param = request_url

        if login_way == 'cookies':
            cookie = self.login().cookies
            try:
                result = requests.put(new_request_url,
                                      json=eval(new_request_param),
                                      headers=eval(request_header),
                                      verify=False,
                                      cookies=cookie)
                if expected_result.encode(
                        'utf-8') in result.content:
                    Case.objects.filter(
                        id=int(number_id)).update(
                        case_result='成功')
                    Case.objects.filter(
                        id=int(number_id)).update(
                        return_result=result.json())
                    RunCases.pass_number += 1
                    try:
                        ReportDetail.objects.create(case_name=case_name,
                                                    request_url=request_url,
                                                    result='PASS',
                                                    test_time=test_time,
                                                    request_type=request_type,
                                                    case_result=result.json(),
                                                    request_param=request_param)
                    except Exception:
                        logging.INFO(traceback.format_exc())
                else:
                    Case.objects.filter(
                        id=int(number_id)).update(
                        case_result='失败')
                    RunCases.fail_number += 1
                    try:
                        ReportDetail.objects.create(case_name=case_name,
                                                    request_url=request_url,
                                                    result='FAIL',
                                                    test_time=test_time,
                                                    request_type=request_type,
                                                    case_result=result.json(),
                                                    request_param=request_param)
                    except Exception:
                        logging.INFO(traceback.format_exc())
            except Exception:
                logging.INFO(traceback.format_exc())
        else:
            jwt = 'JWT ' + self.login().json()['token']
            request_header['Authorization'] = jwt
            try:
                result = requests.put(new_request_url,
                                      json=eval(new_request_param),
                                      headers=eval(request_header),
                                      verify=False)
                if expected_result.encode(
                        'utf-8') in result.content:
                    Case.objects.filter(
                        id=int(number_id)).update(
                        case_result='成功')
                    Case.objects.filter(
                        id=int(number_id)).update(
                        return_result=result.json())
                    RunCases.pass_number += 1
                    try:
                        ReportDetail.objects.create(case_name=case_name,
                                                    request_url=request_url,
                                                    result='PASS',
                                                    test_time=test_time,
                                                    request_type=request_type,
                                                    case_result=result.json(),
                                                    request_param=request_param)
                    except Exception:
                        logging.INFO(traceback.format_exc())
                else:
                    Case.objects.filter(
                        id=int(number_id)).update(
                        case_result='失败')
                    RunCases.fail_number += 1
                    try:
                        ReportDetail.objects.create(case_name=case_name,
                                                    request_url=request_url,
                                                    result='FAIl',
                                                    test_time=test_time,
                                                    request_type=request_type,
                                                    case_result=result.json(),
                                                    request_param=request_param)
                    except Exception:
                        logging.INFO(traceback.format_exc())
            except Exception:
                logging.INFO(traceback.format_exc())

    def post_login_invoking_interface(self):
        new_request_param = ''
        new_request_url = ''
        for index, interface_id in enumerate(eval(invoking_other_interface)):
            try:
                interface_id_str = '[' + str(index + 1) + ']'
                id_res = re.compile('(\[\d\])')
                res_result = id_res.findall(request_param)
                res_url = id_res.findall(request_url)
                # 遍历正则匹配请求参数后的列表
                if len(res_result) > 0:
                    for i in res_result:
                        # 请求参数中对应不同的请求接口
                        if interface_id_str == i:
                            return_result = Case.objects.get(id=interface_id,
                                                             isdelete=True).return_result
                            replace_id = re.compile("(\'id\': )(\d)?")
                            return_id = replace_id.search(return_result)
                            new_request_param = request_param.replace(i,
                                                                      return_id.group(
                                                                          2))
                for i in res_url:
                    # 请求参数中对应不同的请求接口
                    if interface_id_str == i:
                        return_result = Case.objects.get(
                            id=interface_id,
                            isdelete=True).return_result
                        replace_id = re.compile("(\'id\': )(\d)?")
                        return_id = replace_id.search(return_result)
                        new_request_url = request_url.replace(i,
                                                              return_id.group(
                                                                  2))

            except Exception:
                logging.INFO(traceback.format_exc())
        if new_request_param == '':
            new_request_param = request_param
        if new_request_url == '':
            new_request_param = request_url

        if login_way == 'cookies':
            cookie = self.login().cookies
            try:
                result = requests.post(new_request_url,
                                       json=eval(new_request_param),
                                       headers=eval(request_header),
                                       verify=False,
                                       cookies=cookie)
                if expected_result.encode(
                        'utf-8') in result.content:
                    Case.objects.filter(
                        id=int(number_id)).update(
                        case_result='成功')
                    Case.objects.filter(
                        id=int(number_id)).update(
                        return_result=result.json())
                    RunCases.pass_number += 1
                    try:
                        ReportDetail.objects.create(case_name=case_name,
                                                    request_url=request_url,
                                                    result='PASS',
                                                    test_time=test_time,
                                                    request_type=request_type,
                                                    case_result=result.json(),
                                                    request_param=request_param)
                    except Exception:
                        logging.INFO(traceback.format_exc())
                else:
                    Case.objects.filter(
                        id=int(number_id)).update(
                        case_result='失败')
                    RunCases.fail_number += 1
                    try:
                        ReportDetail.objects.create(case_name=case_name,
                                                    request_url=request_url,
                                                    result='FAIL',
                                                    test_time=test_time,
                                                    request_type=request_type,
                                                    case_result=result.json(),
                                                    request_param=request_param)
                    except Exception:
                        logging.INFO(traceback.format_exc())
            except Exception:
                logging.INFO(traceback.format_exc())
        else:
            jwt = 'JWT ' + self.login().json()['token']
            request_header['Authorization'] = jwt
            try:
                result = requests.post(new_request_url,
                                       json=eval(new_request_param),
                                       headers=eval(request_header),
                                       verify=False)
                if expected_result.encode(
                        'utf-8') in result.content:
                    Case.objects.filter(
                        id=int(number_id)).update(
                        case_result='成功')
                    Case.objects.filter(
                        id=int(number_id)).update(
                        return_result=result.json())
                    RunCases.pass_number += 1
                    try:
                        ReportDetail.objects.create(case_name=case_name,
                                                    request_url=request_url,
                                                    result='PASS',
                                                    test_time=test_time,
                                                    request_type=request_type,
                                                    case_result=result.json(),
                                                    request_param=request_param)
                    except Exception:
                        logging.INFO(traceback.format_exc())
                else:
                    Case.objects.filter(
                        id=int(number_id)).update(
                        case_result='失败')
                    RunCases.fail_number += 1
                    try:
                        ReportDetail.objects.create(case_name=case_name,
                                                    request_url=request_url,
                                                    result='FAIL',
                                                    test_time=test_time,
                                                    request_type=request_type,
                                                    case_result=result.json(),
                                                    request_param=request_param)
                    except Exception:
                        logging.INFO(traceback.format_exc())
            except Exception:
                logging.INFO(traceback.format_exc())

    def delete_login_invoking_interface(self):
        new_request_param = ''
        new_request_url = ''
        for index, interface_id in enumerate(eval(invoking_other_interface)):
            try:
                interface_id_str = '[' + str(index + 1) + ']'
                id_res = re.compile('(\[\d\])')
                res_result = id_res.findall(request_param)
                res_url = id_res.findall(request_url)
                # 遍历正则匹配请求参数后的列表
                if len(res_result) > 0:
                    for i in res_result:
                        # 请求参数中对应不同的请求接口
                        if interface_id_str == i:
                            return_result = Case.objects.get(id=interface_id,
                                                             isdelete=True).return_result
                            replace_id = re.compile("(\'id\': )(\d)?")
                            return_id = replace_id.search(return_result)
                            new_request_param = request_param.replace(i,
                                                                      return_id.group(
                                                                          2))
                for i in res_url:
                    # 请求参数中对应不同的请求接口
                    if interface_id_str == i:
                        return_result = Case.objects.get(
                            id=interface_id,
                            isdelete=True).return_result
                        replace_id = re.compile("(\'id\': )(\d)?")
                        return_id = replace_id.search(return_result)
                        new_request_url = request_url.replace(i,
                                                              return_id.group(
                                                                  2))

            except Exception:
                logging.INFO(traceback.format_exc())
        if new_request_param == '':
            new_request_param = request_param
        if new_request_url == '':
            new_request_param = request_url

        if login_way == 'cookies':
            cookie = self.login().cookies
            try:
                result = requests.delete(new_request_url,
                                         json=eval(new_request_param),
                                         headers=eval(request_header),
                                         verify=False,
                                         cookies=cookie)
                if expected_result.encode(
                        'utf-8') in result.content:
                    Case.objects.filter(
                        id=int(number_id)).update(
                        case_result='成功')
                    Case.objects.filter(
                        id=int(number_id)).update(
                        return_result=result.json())
                    RunCases.pass_number += 1
                    try:
                        ReportDetail.objects.create(case_name=case_name,
                                                    request_url=request_url,
                                                    result='PASS',
                                                    test_time=test_time,
                                                    request_type=request_type,
                                                    case_result=result.json(),
                                                    request_param=request_param)
                    except Exception:
                        logging.INFO(traceback.format_exc())
                else:
                    Case.objects.filter(
                        id=int(number_id)).update(
                        case_result='失败')
                    RunCases.fail_number += 1
                    try:
                        ReportDetail.objects.create(case_name=case_name,
                                                    request_url=request_url,
                                                    result='FAIL',
                                                    test_time=test_time,
                                                    request_type=request_type,
                                                    case_result=result.json(),
                                                    request_param=request_param)
                    except Exception:
                        logging.INFO(traceback.format_exc())
            except Exception:
                logging.INFO(traceback.format_exc())
        else:
            jwt = 'JWT ' + self.login().json()['token']
            request_header['Authorization'] = jwt
            try:
                result = requests.delete(new_request_url,
                                         json=eval(new_request_param),
                                         headers=eval(request_header),
                                         verify=False)
                if expected_result.encode(
                        'utf-8') in result.content:
                    Case.objects.filter(
                        id=int(number_id)).update(
                        case_result='成功')
                    Case.objects.filter(
                        id=int(number_id)).update(
                        return_result=result.json())
                    RunCases.pass_number += 1
                    try:
                        ReportDetail.objects.create(case_name=case_name,
                                                    request_url=request_url,
                                                    result='PASS',
                                                    test_time=test_time,
                                                    request_type=request_type,
                                                    case_result=result.json(),
                                                    request_param=request_param)
                    except Exception:
                        logging.INFO(traceback.format_exc())
                else:
                    Case.objects.filter(
                        id=int(number_id)).update(
                        case_result='失败')
                    RunCases.fail_number += 1
                    try:
                        ReportDetail.objects.create(case_name=case_name,
                                                    request_url=request_url,
                                                    result='FAIL',
                                                    test_time=test_time,
                                                    request_type=request_type,
                                                    case_result=result.json(),
                                                    request_param=request_param)
                    except Exception:
                        logging.INFO(traceback.format_exc())
            except Exception:
                logging.INFO(traceback.format_exc())

    def post(self, request):

        global request_type, request_url, request_param, expected_result, \
            invoking_login, request_header, login_way, invoking_other_interface, number_id, case_name, test_time, numbers
        case_ids = request.data
        test_time1 = datetime.datetime.now()

        test_time = datetime.datetime.strftime(test_time1, '%Y-%m-%d %H:%M:%S')
        print(test_time1)
        try:
            for number_id in case_ids['ids']:
                request_type = Case.objects.get(isdelete=True,
                                                id=int(number_id)).request_type
                request_param = Case.objects.get(isdelete=True, id=int(
                    number_id)).request_param
                expected_result = Case.objects.get(isdelete=True,
                                                   id=int(
                                                       number_id)).expected_result
                url = Case.objects.get(isdelete=True, id=int(number_id)).url
                permanent_address = Project.objects.get(isdelete=True,
                                                        project_name=Case.objects.get(
                                                            isdelete=True,
                                                            id=int(
                                                                number_id)).project_name).permanent_address
                request_url = permanent_address + url
                invoking_login = Case.objects.get(isdelete=True,
                                                  id=int(
                                                      number_id)).invoking_login
                request_header = Project.objects.get(isdelete=True,
                                                     project_name=Case.objects.get(
                                                         isdelete=True,
                                                         id=int(
                                                             number_id)).project_name).request_header
                login_way = Project.objects.get(isdelete=True,
                                                project_name=Case.objects.get(
                                                    isdelete=True,
                                                    id=int(
                                                        number_id)).project_name).login_way
                invoking_other_interface = Case.objects.get(isdelete=True,
                                                            id=int(
                                                                number_id)).invoking_other_interface
                case_name = Case.objects.get(isdelete=True,
                                             id=int(
                                                 number_id)).case_name

                if request_param == '':
                    request_param = '{}'

                if invoking_login == '' and request_type == 'get' and \
                        invoking_other_interface == '':
                    self.get_no_login_case()
                if invoking_login == '' and request_type == 'post' and \
                        invoking_other_interface == '':
                    self.post_no_login_case()
                if invoking_login == '' and request_type == 'put' and \
                        invoking_other_interface == '':
                    self.put_no_login_case()
                if invoking_login == '' and request_type == 'delete' and \
                        invoking_other_interface == '':
                    self.delete_no_login_case()

                # 不用登陆、调用其他接口返回信息的情况下
                if invoking_login == '' and request_type == 'get' and \
                        invoking_other_interface != '':
                    self.get_nologin_invoking_interface()
                if invoking_login == '' and request_type == 'post' and \
                        invoking_other_interface != '':
                    self.post_nologin_invoking_interface()
                if invoking_login == '' and request_type == 'put' and \
                        invoking_other_interface != '':
                    self.put_nologin_invoking_interface()
                if invoking_login == '' and request_type == 'delete' and \
                        invoking_other_interface != '':
                    self.delete_nologin_invoking_interface()

                # 要登陆、不调用其他接口返回信息的情况下
                if invoking_login != '' and request_type == 'get' and \
                        invoking_other_interface == '':
                    self.get_login_no_invoking_interface()
                if invoking_login != '' and request_type == 'post' and \
                        invoking_other_interface == '':
                    self.post_login_no_invoking_interface()
                if invoking_login != '' and request_type == 'put' and \
                        invoking_other_interface == '':
                    self.put_login_no_invoking_interface()
                if invoking_login != '' and request_type == 'delete' and \
                        invoking_other_interface == '':
                    self.delete_login_no_invoking_interface()

                # 要登陆、调用其他接口返回信息的情况下
                if invoking_login != '' and request_type == 'get' and \
                        invoking_other_interface != '':
                    self.get_login_invoking_interface()
                if invoking_login != '' and request_type == 'post' and \
                        invoking_other_interface != '':
                    self.post_login_invoking_interface()
                if invoking_login != '' and request_type == 'put' and \
                        invoking_other_interface != '':
                    self.put_login_invoking_interface()
                if invoking_login != '' and request_type == 'delete' and \
                        invoking_other_interface != '':
                    self.delete_login_invoking_interface()
                # threads = []
                # print('开始时间为' + datetime.datetime.now().strftime('%Y%m%d %H%M%S'))
                # for i in numbers:
                #     t = threading.Thread(target=self.select_run_method, args='')
                #     threads.append(t)
                #
                # for i in numbers:
                #     print(i)
                #     threads[i].start()
                #
                # for i in numbers:
                #     print(i)
                #     threads[i].join()
                #
                # print('结束时间为' + datetime.datetime.now().strftime('%Y%m%d %H%M%S'))

                # Report.objects.create(pass_number=RunCases.pass_number,
                #                       fail_number=RunCases.fail_number,
                #                       test_time=test_time)
                # RunCases.pass_number = 0
                # RunCases.fail_number = 0

        except Exception:
            logging.INFO(traceback.format_exc())
        # 不用登陆、不调用其他接口返回信息的情况下
        RunCases.pass_percent = RunCases.pass_number / (
                RunCases.pass_number + RunCases.fail_number) * 100
        RunCases.fail_percent = 100 - RunCases.pass_percent
        Report.objects.create(pass_number=RunCases.pass_number,
                              fail_number=RunCases.fail_number,
                              test_time=test_time)
        RunCases.pass_number = 0
        RunCases.fail_number = 0
        return Response('success')

    # def select_run_method(self):
    #     if invoking_login == '' and request_type == 'get' and \
    #             invoking_other_interface == '':
    #         self.get_no_login_case()
    #     if invoking_login == '' and request_type == 'post' and \
    #             invoking_other_interface == '':
    #         self.post_no_login_case()
    #     if invoking_login == '' and request_type == 'put' and \
    #             invoking_other_interface == '':
    #         self.put_no_login_case()
    #     if invoking_login == '' and request_type == 'delete' and \
    #             invoking_other_interface == '':
    #         self.delete_no_login_case()
    #
    #     # 不用登陆、调用其他接口返回信息的情况下
    #     if invoking_login == '' and request_type == 'get' and \
    #             invoking_other_interface != '':
    #         self.get_nologin_invoking_interface()
    #     if invoking_login == '' and request_type == 'post' and \
    #             invoking_other_interface != '':
    #         self.post_nologin_invoking_interface()
    #     if invoking_login == '' and request_type == 'put' and \
    #             invoking_other_interface != '':
    #         self.put_nologin_invoking_interface()
    #     if invoking_login == '' and request_type == 'delete' and \
    #             invoking_other_interface != '':
    #         self.delete_nologin_invoking_interface()
    #
    #     # 要登陆、不调用其他接口返回信息的情况下
    #     if invoking_login != '' and request_type == 'get' and \
    #             invoking_other_interface == '':
    #         self.get_login_no_invoking_interface()
    #     if invoking_login != '' and request_type == 'post' and \
    #             invoking_other_interface == '':
    #         self.post_login_no_invoking_interface()
    #     if invoking_login != '' and request_type == 'put' and \
    #             invoking_other_interface == '':
    #         self.put_login_no_invoking_interface()
    #     if invoking_login != '' and request_type == 'delete' and \
    #             invoking_other_interface == '':
    #         self.delete_login_no_invoking_interface()
    #
    #     # 要登陆、调用其他接口返回信息的情况下
    #     if invoking_login != '' and request_type == 'get' and \
    #             invoking_other_interface != '':
    #         self.get_login_invoking_interface()
    #     if invoking_login != '' and request_type == 'post' and \
    #             invoking_other_interface != '':
    #         self.post_login_invoking_interface()
    #     if invoking_login != '' and request_type == 'put' and \
    #             invoking_other_interface != '':
    #         self.put_login_invoking_interface()
    #     if invoking_login != '' and request_type == 'delete' and \
    #             invoking_other_interface != '':
    #         self.delete_login_invoking_interface()
