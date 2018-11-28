#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Date: 2018/11/27

from django.urls import path
from django.urls import re_path

from .views import curd

urlpatterns = [
    path("books/", curd.BookView.as_view()),

    re_path("books/(?P<pk>\d+)/", curd.BookDetailView.as_view())
]
