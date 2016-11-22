# _*_coding: utf-8_*_
# coding:utf-8
from rest_framework import viewsets
from serializer import APIServerSerializer
from rest_framework import status
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
import models, requests
from django.core.mail import EmailMultiAlternatives
from django.db import transaction
import webchart
from WXBizMsgCrypt import WXBizMsgCrypt
import xml.etree.cElementTree as ET
import time
from django.shortcuts import render_to_response
from django.http import HttpResponse
from rest_framework_xml.parsers import XMLParser
from rest_framework.decorators import parser_classes


class APIServerViewSet(viewsets.ModelViewSet):
    queryset = models.APIServer.objects.all()
    serializer_class = APIServerSerializer


@api_view(['GET', 'POST'])
# @permission_classes((permissions.IsAuthenticated,))
@transaction.atomic
def api_servers(request):
    if request.method == 'GET':
        info_list = models.APIServer.objects.all()
        serializer = APIServerSerializer(info_list, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        send_user = str(request.user)
        api_data = request.data
        api_email = api_data['to_email']
        print '=============>', api_data
        # 生成邮件list列表
        to_email = str(api_email).split(',')
        print '================email', api_email
        print '================ to email', to_email
        # print '================ type email', type(to_email)

        # Start Email
        email_subject = api_data['email_subject']
        from_email = 'farmer_2012@163.com'
        email_content = api_data['email_content']
        phone_content = email_content
        msg = EmailMultiAlternatives(email_subject, email_content, from_email, to_email)

        print '==============email_content========================', email_content

        # End Email
        # send = msg.send()

        # Start Msg Conf for Public
        access_token = 'Ops'
        current_user_id = '123'
        key = '^%&&^&GHGH#huhuyhu3yru'
        msg_url = "http://123.56.248.36:9998/sb/openapi/inner_sms"
        # End Msg

        # Define
        # save_email_msg = models.APIServer()
        # save_email_msg.send_user = send_user
        # save_email_msg.email_subject = email_subject
        # save_email_msg.email_content = email_content
        # save_email_msg.to_email = e
        # save_email_msg.phone_number = phone_number
        # save_email_msg.phone_content = phone_content

        for e in to_email:
            query_phone = models.APIUser.objects.filter(user_email=e).values('user_phone')
            phone_number = (list(query_phone))[0]['user_phone']
            # print '===========为空===========>',e
            # print '=============电话号码=====>', phone_number
            save_email_msg = models.APIServer()
            save_email_msg.send_user = send_user
            save_email_msg.email_subject = email_subject
            save_email_msg.email_content = email_content
            save_email_msg.phone_content = phone_content
            save_email_msg.to_email = e
            save_email_msg.phone_number = phone_number
            phone_content = phone_content
            save_email_msg.save()

            payload = {
                'access_token': access_token,
                'current_user_id': current_user_id,
                'key': key,
                'phone': phone_number,
                'msg': phone_content
            }
            # msg.send()
            # response = requests.request("POST", msg_url, data=payload)
            # print response.text

            # End send Msg
            # print '------------------------>', datetime.datetime.now()
        # wx_task = webchart.Webchart()
        # wx_task.webchart(email_content)
        return Response(u'发送邮件和短信成功', status=status.HTTP_201_CREATED)
        # return Response(u'发送失败', status.HTTP_400_BAD_REQUEST)
        #  return Response(u'错误的请求')


@api_view(['GET', 'POST'])
@parser_classes((XMLParser,))
def wx_api(request):
    if request.method == 'GET':
        # 假设企业在公众平台上设置的参数如下

        print request.GET
        sToken = ""
        sEncodingAESKey = ""
        sCorpID = ""
        wxcpt = WXBizMsgCrypt(sToken, sEncodingAESKey, sCorpID)

        sVerifyMsgSig = request.GET.get("msg_signature")
        sVerifyTimeStamp = request.GET.get("timestamp")
        sVerifyNonce = request.GET.get("nonce")
        sVerifyEchoStr = request.GET.get("echostr")
        ret, sEchoStr = wxcpt.VerifyURL(sVerifyMsgSig, sVerifyTimeStamp, sVerifyNonce, sVerifyEchoStr)
        if ret != 0:
            print "ERR: VerifyURL ret: " + str(ret)
            return Response("Failed", status.HTTP_400_BAD_REQUEST)
        print type(sEchoStr)
        return HttpResponse(sEchoStr)
    else:
        # print request.POST
        # print request.body
        sToken = ""
        sEncodingAESKey = ""
        sCorpID = ""
        wxcpt = WXBizMsgCrypt(sToken, sEncodingAESKey, sCorpID)

        sReqMsgSig = request.query_params.get("msg_signature")
        sReqTimeStamp = request.query_params.get("timestamp")
        sReqNonce = request.query_params.get("nonce")

        sReqData = request.body
        ret, sMsg= wxcpt.DecryptMsg(sReqData, sReqMsgSig, sReqTimeStamp, sReqNonce)
        if ret != 0:
            print "ERR: VerifyURL ret: " + str(ret)
            return Response("Failed", status.HTTP_400_BAD_REQUEST)
        content = ET.fromstring(sMsg).find("Content").text
        print content
        ToUserName = ET.fromstring(sMsg).find("FromUserName").text
        timestamp = str(int(time.time()))
        FromUserName = sCorpID
        content = '成功'
        sRespData = '''<xml>
                        <ToUserName><![CDATA[''' + ToUserName + ''']]></ToUserName>
                        <FromUserName><![CDATA[''' + FromUserName + ''']]></FromUserName>
                        <CreateTime>''' + timestamp + '''</CreateTime>
                        <MsgType><![CDATA[text]]></MsgType>
                        <Content><![CDATA[''' + content + ''']]></Content>
                        <MsgId>1234567890123456</MsgId>
                        <AgentID>0</AgentID>
                        </xml>'''
        ret, sEncryptMsg = wxcpt.EncryptMsg(sRespData, sReqNonce, timestamp)
        if ret != 0:
            print "ERR: VerifyURL ret: " + str(ret)
            return Response("Failed", status.HTTP_400_BAD_REQUEST)
        return HttpResponse(sEncryptMsg)





