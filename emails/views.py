# _*_coding: utf-8_*_

from django.shortcuts import HttpResponse, render
from django.core.mail import EmailMultiAlternatives
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response
from django.template import RequestContext
import requests


def send_email(request):
    if request.method == "POST":
        print request.POST
        subject = request.POST.get('content')
        from_email = request.POST.get('from-email')
        to = request.POST.get('to-email')
        text_content = request.POST.get('text-content')

        # 发送链接格式：u'<b>激活链接：</b><a href="http://......">http://....</a>'
        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        # msg.attach_alternative(text_content, 'text/html')
        msg.send()

        return HttpResponse(u'发送邮件成功')
    return render(request, 'sendemail.html')


def send_msg(request):
    if request.method == "POST":
        access_token = 'Ops'
        current_user_id = '123'
        key = '^%&&^&GHGH#huhuyhu3yru'
        phone = request.POST.get('phone')
        msg = request.POST.get('msg')

        msg_url = "http://119.57.164.68:9998/sb/openapi/inner_sms"

        payload = {
            'access_token': access_token,
            'current_user_id': current_user_id,
            'key': key,
            'phone': phone,
            'msg': msg
        }
        response = requests.request("POST", msg_url, data=payload)
        print(response.text)
        return HttpResponse(u'发送短信成功')
    return render(request, 'sendmsg.html')

