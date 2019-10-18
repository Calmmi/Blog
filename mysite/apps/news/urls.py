#!/usr/bin/python3.7
# -*- coding:utf-8 -*-
# Auth:Calm  Date : 2019-10-18 20:03

from django.urls import path
from news import views

app_name = "news"

urlpatterns = [
    path("index/",views.index_view,name="news_index")
]