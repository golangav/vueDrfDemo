#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Date: 2018/11/27

from rest_framework.generics import ListAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.response import Response

from web import models
from ..serializers import curd


class BookView(ListAPIView):
    queryset = models.Book.objects.all()
    serializer_class = curd.BookSerializer

    fields = [
        {
            'key': 'id',
            'label': 'ID',
        },
        {
            'key': 'title',
            'label': '标题'
        },
        {
            'key': 'price',
            'label': '价格'
        },
        {
            'key': 'publish',
            'label': '出版社'
        },
        {
            'key': 'pub_date',
            'label': '出版日期'
        },
        {
            'key': 'authors',
            'label': '作者们'
        },
        {
            'key': 'handle',
            'label': '操作'
        }
    ]

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            paginated_data = self.paginator.get_paginated_data(serializer.data)
            return Response({
                "fields": self.fields,
                "result": paginated_data
            })

        serializer = self.get_serializer(queryset, many=True)
        return Response({
            "fields": self.fields,
            "result": serializer.data
        })


class BookDetailView(RetrieveUpdateDestroyAPIView):
    queryset = models.Book.objects.all()
    serializer_class = curd.BookSerializer

    authentication_classes = ()
    permission_classes = ()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({})
