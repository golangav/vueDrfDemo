#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Date: 2018/11/27

from django.views.generic import TemplateView


class IndexView(TemplateView):

    """
    首页视图
    """

    template_name = "web/index.html"

    extra_context = {
        "title": "欢迎使用图书管理系统"
    }


class BookDetailView(TemplateView):

    template_name = "web/detail.html"

    extra_context = {
        "title": "书籍详情页"
    }
