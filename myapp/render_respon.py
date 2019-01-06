# -*- coding:utf-8 -*-
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from collections import OrderedDict

class LargeResultsSetPagination(LimitOffsetPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 10000

    def get_paginated_response(self, results):
        code = 0
        msg = ''
        if Response.status_code == 200 or Response.status_code == 204:
            code = 200
            msg = 'success'
        # if not results:
        #     code = 404
        #     msg = "data not found"
        if Response.status_code == 400:
            msg = results

        return Response(OrderedDict([
            ('code', code),
            ('msg', msg),
            ('count', self.count),
            ('results', results),
        ]))
