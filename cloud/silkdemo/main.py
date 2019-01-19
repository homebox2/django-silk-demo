# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

from rest_framework.views import APIView
from rest_framework.response import Response
from cloud.silkdemo.models.restaurant import Restaurant


class TestView(APIView):
    def get(self, requests):
        return Response("Hello I'm TestView")
