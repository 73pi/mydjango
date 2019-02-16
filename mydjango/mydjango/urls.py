"""mydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from learn import views as learn_view

urlpatterns = [
    url(r'^template_adv/', learn_view.template_adv),
    url(r'^first_template/', learn_view.frist_template, name='home'),
    url(r'^new_add/(\d+)/(\d+)/$', learn_view.add2, name='add2'),
    url(r'^add/(\d+)/(\d+)/$', learn_view.old_too_new_url),
    url(r'^add/$', learn_view.add, name='add'),
    url(r'^first/', learn_view.index),
    url(r'^admin/', include(admin.site.urls)),
]
