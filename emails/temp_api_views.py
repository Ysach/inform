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


class APIServerViewSet(viewsets.ModelViewSet):
    queryset = models.APIServer.objects.all()
    serializer_class = APIServerSerializer


@api_view(['GET', 'POST'])
@permission_classes((permissions.IsAuthenticated,))
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
        print '================ type email', type(to_email)

        # Start Email
        email_subject = api_data['email_subject']
        from_email = 'farmer_2012@163.com'
        email_content = api_data['email_content']
        phone_content = email_content
        msg = EmailMultiAlternatives(email_subject, email_content, from_email, to_email)

        # End Email
        # send = msg.send()

        # Start Msg Conf for Public
        access_token = 'Ops'
        current_user_id = '123'
        key = '^%&&^&GHGH#huhuyhu3yru'
        msg_url = "http://119.57.164.68:9998/sb/openapi/inner_sms"
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
            print '===========为空===========>',e
            save_email_msg = models.APIServer()
            save_email_msg.send_user = send_user
            save_email_msg.email_subject = email_subject
            save_email_msg.email_content = email_content
            save_email_msg.phone_content = phone_content
            save_email_msg.to_email = e
            save_email_msg.phone_number = phone_number
            save_email_msg.save()

            '''
            if phone_number == '':
                msg.send()
                save_email_msg.save()

            else:
                payload = {
                    'access_token': access_token,
                    'current_user_id': current_user_id,
                    'key': key,
                    'phone': phone_number,
                    'msg': phone_content
                }

                # requests.request("POST", msg_url, data=payload)
                # End send Msg
                save_email_msg.to_email = e
                save_email_msg.phone_number = phone_number
                save_email_msg.save()

                print '=======email content======>', email_content
                print '=======email subject======>', email_subject
                print '=======phone number======>', phone_number
                # print '------------------------>', datetime.datetime.now()
                '''
        return Response(u'发送邮件和短信成功', status=status.HTTP_201_CREATED)
        # return Response(u'发送失败', status.HTTP_400_BAD_REQUEST)
        #  return Response(u'错误的请求')

