# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

from django.conf.urls import url

from cloud.silkdemo.main import TestView


urlpatterns = [
    url(r'^test', TestView.as_view())
]
