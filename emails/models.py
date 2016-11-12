# _*_coding: utf-8_*_
# coding:utf-8
from django.db import models

# Create your models here.


class EmailUser(models.Model):
    subject = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
    content = models.CharField(max_length=600)


class UserAuth(models.Model):
    owner = models.ForeignKey('auth.User', related_name='auth_users')
    highlighted = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
            ordering = ('created',)


class MsgInfo(models.Model):
    phone = models.CharField(max_length=8000)
    msg = models.CharField(max_length=100)
    # email = models.ForeignKey('EmailInfo')
    time = models.DateTimeField(auto_now_add=True)


class EmailInfo(models.Model):
    subject = models.CharField(max_length=64)
    email = models.CharField(max_length=8000)
    content = models.CharField(max_length=600)
    username = models.CharField(max_length=64)
    time = models.DateTimeField(auto_now_add=True)


# 定义全局Email 和 Msg的数据库表
class APIServer(models.Model):
    send_user = models.CharField(max_length=32)
    email_subject = models.CharField(max_length=255)
    to_email = models.EmailField()
    email_content = models.TextField()
    phone_number = models.CharField(max_length=11, null=True, blank=True)
    phone_content = models.TextField(null=True, blank=True)
    send_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = u'API后台'
        verbose_name_plural = u'API后台'


class APIUser(models.Model):
    user_email = models.EmailField(unique=True)
    user_phone = models.CharField(max_length=11, null=True, blank=True)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = u'API授权用户'
        verbose_name_plural = u'API授权用户'


# 全局数据库表配置结束


