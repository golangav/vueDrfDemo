#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Date: 2018/11/27

from rest_framework import serializers
from rest_framework.settings import api_settings

from web import models


class BookSerializer(serializers.ModelSerializer):

    pub_date = serializers.DateTimeField(format=api_settings.DATETIME_FORMAT)
    publish = serializers.CharField(source="publish.name")
    # 操作
    handle = serializers.SerializerMethodField()

    HANDLE_HTML = '<button class="btn btn-danger btn-xs" pk={}>删除</button>'

    class Meta:
        model = models.Book
        fields = "__all__"

    def get_handle(self, instance):
        # 定制删除 `button`
        return self.HANDLE_HTML.format(instance.pk)

    def to_representation(self, instance):
        # 获取原始序列化数据
        data = super(BookSerializer, self).to_representation(instance)

        data["authors"] = "，".join(
            author.name for author in instance.authors.only("name").iterator()
        )

        return data
