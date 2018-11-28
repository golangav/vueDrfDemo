#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Date: 2018/11/27

from django.urls import re_path

from .views import basic

urlpatterns = [
    re_path('^$', basic.IndexView.as_view()),
    re_path('^books/(?P<pk>\d+)/$', basic.BookDetailView.as_view())
]

