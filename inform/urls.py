"""inform URL Configuration

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
import os
from django.contrib import admin
from emails import urls, views
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^send_email/$', views.send_email, name="send_email"),
    url(r'^send_msg/$', views.send_msg, name="send_msg"),
    # url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'D:\BaiduYunDownload\project\inform\statics'}),
    url(r'^api/', include(urls)),

]
