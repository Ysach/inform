# _*_coding: utf-8_*_
# coding:utf-8
from rest_framework import viewsets
from serializer import EmailSerializer, UserSerializer, EmailInfoSerializer, MsgInfoSerializer
from rest_framework import status
from rest_framework import permissions
from rest_permissions import IsOwnerOrReadOnly
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
import models, requests
from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from rest_framework import generics
import datetime
import json


class EmailViewSet(viewsets.ModelViewSet):
    queryset = models.EmailUser.objects.all()
    serializer_class = EmailSerializer
    # permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = (permissions.IsAuthenticated,)


class EmailServerViewSet(viewsets.ModelViewSet):
    queryset = models.EmailInfo.objects.all()
    serializer_class = EmailInfoSerializer
    # permission_classes = (permissions.IsAuthenticated,)


class MsgServerViewSet(viewsets.ModelViewSet):
    queryset = models.MsgInfo.objects.all()
    serializer_class = MsgInfoSerializer
    # permission_classes = (permissions.IsAuthenticated,)


@api_view(['GET', 'POST'])
@permission_classes((permissions.IsAuthenticated,))
def email_servers(request):
    if request.method == 'GET':
        info_list = models.EmailInfo.objects.all()
        serializer = EmailInfoSerializer(info_list, many=True)
        # data = serializer.data
        # print '==========>', data
        # print '+++++++++++++++++++++', type(data)
        # content = JSONRenderer().render(data)
        # print '-------------->', type(content), '----->', content
        return Response(serializer.data)

    elif request.method == 'POST':

        # 获取发送POST请求的用户，验证过后的request.auth结果为None

        username = str(request.user)

        # 使用Rest Frame 对POST方法数据处理时间 1-2ms，这里去掉，用其他方式
        # serializer = EmailInfoSerializer(data=request.data)

        email_data = request.data
        email_save = email_data['email']
        print '=============>', email_data
        # 生成邮件list列表
        email_temp = str(email_save).split(',')
        print '================email', email_save
        # if serializer.is_valid():
        #    serializer.save时间比下面的时间多出50-79ms，去掉
        #    serializer.save()
        #    while True:

        subject = email_data['subject']
        from_email = 'farmer_2012@163.com'
        email = email_temp
        content = email_data['content']
        msg = EmailMultiAlternatives(subject, content, from_email, email)
        # send = msg.send()
        e = models.APIUser.objects.filter(user_email=email_save).values('user_phone')
        print '=============E is =========', e, 'pppppppppppppppp', type(e)

        if (list(e))[0]['user_phone'] == '':
            print 'eeeee'
        else:
            p = ((list(e))[0]['user_phone'])

            print 'int=======', type(p), p

        if msg:
            # for e in email_temp:
            save = models.EmailInfo()
            save.subject = subject
            save.email = email_save
            save.username = username
            save.content = content
            save.save()
            return Response(u'发送邮件成功', status=status.HTTP_201_CREATED)
        return Response(u'发送失败', status.HTTP_400_BAD_REQUEST)

    return Response(u'错误的请求')


@api_view(['GET', 'POST'])
@permission_classes((permissions.IsAuthenticated,))
def msg_servers(request):
    if request.method == 'GET':
        msg_list = models.MsgInfo.objects.all()
        serializer = MsgInfoSerializer(msg_list, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MsgInfoSerializer(data=request.data)
        msg_data = request.data
        if serializer.is_valid():
            serializer.save()

            while True:
                access_token = 'Ops'
                current_user_id = '123'
                key = '^%&&^&GHGH#huhuyhu3yru'
                phone = msg_data['phone']
                msg = msg_data['msg']

                msg_url = "http://119.57.164.68:9998/sb/openapi/inner_sms"

                payload = {
                    'access_token': access_token,
                    'current_user_id': current_user_id,
                    'key': key,
                    'phone': phone,
                    'msg': msg
                }
                response = requests.request("POST", msg_url, data=payload)
                return Response('短信发送成功')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

