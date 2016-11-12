# _*_coding: utf-8_*_
from django.conf.urls import url, include
from rest_framework import routers
import rest_views as views
import api_views

router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
# router.register(r'email', views.EmailServerViewSet)
# router.register(r'msg', views.MsgServerViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^email/$', views.email_servers),
    url(r'^msg/$', views.msg_servers),
    url(r'^api_server/$', api_views.api_servers),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
