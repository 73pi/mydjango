# -*- coding: utf-8 -*-#

from django.contrib import admin
from .models import People

# 将数据表加到服务器网页中
admin.site.register(People)

