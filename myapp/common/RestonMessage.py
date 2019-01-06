# -*- coding:utf-8 -*-


def respon_200():
    code_200 = {'code': 200, 'message': 'success'}
    return code_200


def respon_417():
    code_417 = {'code': 417, 'message': '参数错误'}
    return code_417


def respon_404():
    code_404 = {'code': 404, 'message': '访问数据不存在'}
    return code_404


def respon_204():
    code_404 = {'code': 204, 'message': '删除对象成功'}
    return code_404
