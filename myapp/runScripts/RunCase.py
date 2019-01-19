# -*- coding:utf-8 -*-
from rest_framework.views import APIView
from ..models import Case, Project
import logging
import requests
from rest_framework.response import Response
import re
import logging
import traceback

logging.basicConfig(filename='runcase.txt', level=logging.INFO)


class RunCase(APIView):
    # 登陆接口返回数据
    def login(self):
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
                               headers=eval(login_request_header), verify=False)
        # if login_login_way == 'cookies':
        #     return result.cookies
        # else:
        #     jwt = 'JWT ' + result.json()['token']
        #     return jwt
        return result

    # 不调用登陆、其他接口返回数据
    def get_no_login_case(self):
        result = requests.get(request_url, params=eval(request_param),
                              headers=eval(request_header), verify=False)
        if expected_result.encode('utf-8') in result.content:
            Case.objects.filter(id=int(number_id['suite_id'])).update(
                case_result='成功')
            Case.objects.filter(id=int(number_id['suite_id'])).update(
                return_result=result.json())
        else:
            Case.objects.filter(id=int(number_id['suite_id'])).update(
                case_result='失败')

    def post_no_login_case(self):
        result = requests.post(request_url, json=eval(request_param),
                               headers=eval(request_header), verify=False)
        print(result.cookies)
        if expected_result.encode('utf-8') in result.content:
            Case.objects.filter(id=int(number_id['suite_id'])).update(
                case_result='成功')
            Case.objects.filter(id=int(number_id['suite_id'])).update(
                return_result=result.json())
        else:
            Case.objects.filter(id=int(number_id['suite_id'])).update(
                case_result='失败')

    def put_no_login_case(self):
        result = requests.put(request_url, json=eval(request_param),
                              headers=eval(request_header), verify=False)
        if expected_result.encode('utf-8') in result.content:
            Case.objects.filter(id=int(number_id['suite_id'])).update(
                case_result='成功')
            Case.objects.filter(id=int(number_id['suite_id'])).update(
                return_result=result.json())
        else:
            Case.objects.filter(id=int(number_id['suite_id'])).update(
                case_result='失败')

    def delete_no_login_case(self):
        result = requests.delete(request_url, json=eval(request_param),
                                 headers=eval(request_header), verify=False)
        if expected_result.encode('utf-8') in result.content:
            Case.objects.filter(id=int(number_id['suite_id'])).update(
                case_result='成功')
            Case.objects.filter(id=int(number_id['suite_id'])).update(
                return_result=result.json())
        else:
            Case.objects.filter(id=int(number_id['suite_id'])).update(
                case_result='失败')

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
                                id=int(number_id['suite_id'])).update(
                                case_result='成功')
                            Case.objects.filter(
                                id=int(number_id['suite_id'])).update(
                                return_result=result.json())
                        else:
                            Case.objects.filter(
                                id=int(number_id['suite_id'])).update(
                                case_result='失败')
            except Exception as e:
                logging.debug(e)

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
                                id=int(number_id['suite_id'])).update(
                                case_result='成功')
                            Case.objects.filter(
                                id=int(number_id['suite_id'])).update(
                                return_result=result.json())
                        else:
                            Case.objects.filter(
                                id=int(number_id['suite_id'])).update(
                                case_result='失败')
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
                                id=int(number_id['suite_id'])).update(
                                case_result='成功')
                            Case.objects.filter(
                                id=int(number_id['suite_id'])).update(
                                return_result=result.json())
                        else:
                            Case.objects.filter(
                                id=int(number_id['suite_id'])).update(
                                case_result='失败')
            except Exception as e:
                logging.INFO(traceback.format_exc())

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

        result = requests.delete(new_request_url,
                                 json=eval(new_request_param),
                                 headers=eval(request_header),
                                 verify=False)
        if expected_result.encode(
                'utf-8') in result.content:
            Case.objects.filter(
                id=int(number_id['suite_id'])).update(
                case_result='成功')
            Case.objects.filter(
                id=int(number_id['suite_id'])).update(
                return_result=result.json())
        else:
            Case.objects.filter(
                id=int(number_id['suite_id'])).update(
                case_result='失败')

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
            result = requests.get(request_url, params=eval(request_param),
                                  headers=eval(request_header), verify=False,
                                  cookies=cookie)
            if expected_result.encode('utf-8') in result.content:
                Case.objects.filter(id=int(number_id['suite_id'])).update(
                    case_result='成功')
                Case.objects.filter(id=int(number_id['suite_id'])).update(
                    return_result=result.json())
            else:
                Case.objects.filter(id=int(number_id['suite_id'])).update(
                    case_result='失败')
        else:
            jwt = 'JWT ' + self.login().json()['token']
            request_header['Authorization'] = jwt
            result = requests.get(request_url, params=eval(request_param),
                                  headers=eval(request_header), verify=False)
            if expected_result.encode('utf-8') in result.content:
                Case.objects.filter(id=int(number_id['suite_id'])).update(
                    case_result='成功')
                Case.objects.filter(id=int(number_id['suite_id'])).update(
                    return_result=result.json())
            else:
                Case.objects.filter(id=int(number_id['suite_id'])).update(
                    case_result='失败')

    def post_login_no_invoking_interface(self):

        if login_way == 'cookies':
            cookie = self.login().cookies
            result = requests.post(request_url, json=eval(request_param),
                                   headers=eval(request_header), verify=False,
                                   cookies=cookie)
            if expected_result.encode('utf-8') in result.content:
                Case.objects.filter(id=int(number_id['suite_id'])).update(
                    case_result='成功')
                Case.objects.filter(id=int(number_id['suite_id'])).update(
                    return_result=result.json())
            else:
                Case.objects.filter(id=int(number_id['suite_id'])).update(
                    case_result='失败')
        else:
            jwt = 'JWT ' + self.login().json()['token']
            request_header['Authorization'] = jwt
            result = requests.post(request_url, json=eval(request_param),
                                   headers=eval(request_header), verify=False)
            if expected_result.encode('utf-8') in result.content:
                Case.objects.filter(id=int(number_id['suite_id'])).update(
                    case_result='成功')
                Case.objects.filter(id=int(number_id['suite_id'])).update(
                    return_result=result.json())
            else:
                Case.objects.filter(id=int(number_id['suite_id'])).update(
                    case_result='失败')

    def put_login_no_invoking_interface(self):

        if login_way == 'cookies':
            cookie = self.login().cookies
            result = requests.put(request_url, json=eval(request_param),
                                  headers=eval(request_header), verify=False,
                                  cookies=cookie)
            if expected_result.encode('utf-8') in result.content:
                Case.objects.filter(id=int(number_id['suite_id'])).update(
                    case_result='成功')
                Case.objects.filter(id=int(number_id['suite_id'])).update(
                    return_result=result.json())
            else:
                Case.objects.filter(id=int(number_id['suite_id'])).update(
                    case_result='失败')
        else:
            jwt = 'JWT ' + self.login().json()['token']
            request_header['Authorization'] = jwt
            result = requests.put(request_url, json=eval(request_param),
                                  headers=eval(request_header), verify=False)
            if expected_result.encode('utf-8') in result.content:
                Case.objects.filter(id=int(number_id['suite_id'])).update(
                    case_result='成功')
                Case.objects.filter(id=int(number_id['suite_id'])).update(
                    return_result=result.json())
            else:
                Case.objects.filter(id=int(number_id['suite_id'])).update(
                    case_result='失败')

    def delete_login_no_invoking_interface(self):

        if login_way == 'cookies':
            cookie = self.login().cookies
            result = requests.delete(request_url, json=eval(request_param),
                                     headers=eval(request_header), verify=False,
                                     cookies=cookie)
            if expected_result.encode('utf-8') in result.content:
                Case.objects.filter(id=int(number_id['suite_id'])).update(
                    case_result='成功')
                Case.objects.filter(id=int(number_id['suite_id'])).update(
                    return_result=result.json())
            else:
                Case.objects.filter(id=int(number_id['suite_id'])).update(
                    case_result='失败')
        else:
            jwt = 'JWT ' + self.login().json()['token']
            request_header['Authorization'] = jwt
            result = requests.delete(request_url, json=eval(request_param),
                                     headers=eval(request_header), verify=False)
            if expected_result.encode('utf-8') in result.content:
                Case.objects.filter(id=int(number_id['suite_id'])).update(
                    case_result='成功')
                Case.objects.filter(id=int(number_id['suite_id'])).update(
                    return_result=result.json())
            else:
                Case.objects.filter(id=int(number_id['suite_id'])).update(
                    case_result='失败')

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
            result = requests.get(new_request_url,
                                  params=eval(new_request_param),
                                  headers=eval(request_header),
                                  verify=False,
                                  cookies=cookie)
            if expected_result.encode(
                    'utf-8') in result.content:
                Case.objects.filter(
                    id=int(number_id['suite_id'])).update(
                    case_result='成功')
                Case.objects.filter(
                    id=int(number_id['suite_id'])).update(
                    return_result=result.json())
            else:
                Case.objects.filter(
                    id=int(number_id['suite_id'])).update(
                    case_result='失败')

        else:
            jwt = 'JWT ' + self.login().json()['token']
            request_header['Authorization'] = jwt
            result = requests.put(new_request_url,
                                  params=eval(new_request_param),
                                  headers=eval(request_header),
                                  verify=False)
            if expected_result.encode(
                    'utf-8') in result.content:
                Case.objects.filter(
                    id=int(number_id['suite_id'])).update(
                    case_result='成功')
                Case.objects.filter(
                    id=int(number_id['suite_id'])).update(
                    return_result=result.json())
            else:
                Case.objects.filter(
                    id=int(number_id['suite_id'])).update(
                    case_result='失败')

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
            result = requests.put(new_request_url,
                                  json=eval(new_request_param),
                                  headers=eval(request_header),
                                  verify=False,
                                  cookies=cookie)
            if expected_result.encode(
                    'utf-8') in result.content:
                Case.objects.filter(
                    id=int(number_id['suite_id'])).update(
                    case_result='成功')
                Case.objects.filter(
                    id=int(number_id['suite_id'])).update(
                    return_result=result.json())
            else:
                Case.objects.filter(
                    id=int(number_id['suite_id'])).update(
                    case_result='失败')
        else:
            jwt = 'JWT ' + self.login().json()['token']
            request_header['Authorization'] = jwt
            result = requests.put(new_request_url,
                                  json=eval(new_request_param),
                                  headers=eval(request_header),
                                  verify=False)
            if expected_result.encode(
                    'utf-8') in result.content:
                Case.objects.filter(
                    id=int(number_id['suite_id'])).update(
                    case_result='成功')
                Case.objects.filter(
                    id=int(number_id['suite_id'])).update(
                    return_result=result.json())
            else:
                Case.objects.filter(
                    id=int(number_id['suite_id'])).update(
                    case_result='失败')

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
            result = requests.post(new_request_url,
                                   json=eval(new_request_param),
                                   headers=eval(request_header),
                                   verify=False,
                                   cookies=cookie)
            if expected_result.encode(
                    'utf-8') in result.content:
                Case.objects.filter(
                    id=int(number_id['suite_id'])).update(
                    case_result='成功')
                Case.objects.filter(
                    id=int(number_id['suite_id'])).update(
                    return_result=result.json())
            else:
                Case.objects.filter(
                    id=int(number_id['suite_id'])).update(
                    case_result='失败')
        else:
            jwt = 'JWT ' + self.login().json()['token']
            request_header['Authorization'] = jwt
            result = requests.post(new_request_url,
                                   json=eval(new_request_param),
                                   headers=eval(request_header),
                                   verify=False)
            if expected_result.encode(
                    'utf-8') in result.content:
                Case.objects.filter(
                    id=int(number_id['suite_id'])).update(
                    case_result='成功')
                Case.objects.filter(
                    id=int(number_id['suite_id'])).update(
                    return_result=result.json())
            else:
                Case.objects.filter(
                    id=int(number_id['suite_id'])).update(
                    case_result='失败')

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
            result = requests.delete(new_request_url,
                                     json=eval(new_request_param),
                                     headers=eval(request_header),
                                     verify=False,
                                     cookies=cookie)
            if expected_result.encode(
                    'utf-8') in result.content:
                Case.objects.filter(
                    id=int(number_id['suite_id'])).update(
                    case_result='成功')
                Case.objects.filter(
                    id=int(number_id['suite_id'])).update(
                    return_result=result.json())
            else:
                Case.objects.filter(
                    id=int(number_id['suite_id'])).update(
                    case_result='失败')
        else:
            jwt = 'JWT ' + self.login().json()['token']
            request_header['Authorization'] = jwt
            result = requests.delete(new_request_url,
                                     json=eval(new_request_param),
                                     headers=eval(request_header),
                                     verify=False)
            if expected_result.encode(
                    'utf-8') in result.content:
                Case.objects.filter(
                    id=int(number_id['suite_id'])).update(
                    case_result='成功')
                Case.objects.filter(
                    id=int(number_id['suite_id'])).update(
                    return_result=result.json())
            else:
                Case.objects.filter(
                    id=int(number_id['suite_id'])).update(
                    case_result='失败')

    def post(self, request):
        global request_type, request_url, request_param, expected_result, \
            invoking_login, request_header, login_way, invoking_other_interface, number_id
        try:

            number_id = request.data
            request_type = Case.objects.get(isdelete=True,
                                            id=int(number_id[
                                                       'suite_id'])).request_type
            request_param = Case.objects.get(isdelete=True, id=int(number_id[
                                                                       'suite_id'])).request_param
            expected_result = Case.objects.get(isdelete=True, id=int(number_id[
                                                                         'suite_id'])).expected_result
            url = Case.objects.get(isdelete=True, id=int(number_id[
                                                             'suite_id'])).url
            permanent_address = Project.objects.get(isdelete=True,
                                                    project_name=Case.objects.get(
                                                        isdelete=True,
                                                        id=int(number_id[
                                                                   'suite_id'])).project_name).permanent_address
            request_url = permanent_address + url
            invoking_login = Case.objects.get(isdelete=True, id=int(number_id[
                                                                        'suite_id'])).invoking_login
            request_header = Project.objects.get(isdelete=True,
                                                 project_name=Case.objects.get(
                                                     isdelete=True,
                                                     id=int(number_id[
                                                                'suite_id'])).project_name).request_header
            login_way = Project.objects.get(isdelete=True,
                                            project_name=Case.objects.get(
                                                isdelete=True,
                                                id=int(number_id[
                                                           'suite_id'])).project_name).login_way
            invoking_other_interface = Case.objects.get(isdelete=True,
                                                        id=int(number_id[
                                                                   'suite_id'])).invoking_other_interface

            if request_param == '':
                request_param = '{}'
        except Exception:
            logging.INFO(traceback.format_exc())
        # 不用登陆、不调用其他接口返回信息的情况下
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
        return Response('success')
