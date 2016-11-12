# _*_coding:utf-8_*_
__author__ = 'farmer'
import requests
import json


class Webchart(object):

    def webchart(self, wx_content):

        # 设置corpid和corpsecret值
        corpid = 'wx69584434aea8351a'
        corpsecret = 'qJ_97E8ZWb8Iymv0iv8-Dcnat38Mf0iN5or3-Pmn-3cXydSD7aVUVbZClEEOp2L9'

        # 微信send  get  msg url连接地址
        urlsend = "https://qyapi.weixin.qq.com/cgi-bin/message/send"
        urlget = "https://qyapi.weixin.qq.com/cgi-bin/gettoken?"

        # 微信get 参数字典
        getval = {'corpid': corpid, 'corpsecret': corpsecret}

        # 请求来获取access_token数值
        get = requests.request("GET", urlget, params=getval)

        # 请求返回json格式的数值
        res = get.text

        # 获取access_token的值
        dict_res = json.loads(res)['access_token']
        # access_token值
        querystring = {'access_token': dict_res}

        # 传输的参数值

        # wx_content = '我的测试'
        # wx_content = wx_content

        payload = {
                    "touser": "lvfarmer",
                    "msgtype": "text",
                    "agentid": "0",
                    "text": {"content": wx_content},
                    "safe": "0"
                }

        # 生成json串主要处理中文乱码
        data = json.dumps(payload).decode('unicode-escape').encode('utf8')
        # 或者使用ensure_ascii
        # data = json.dumps(payload, ensure_ascii=False, encoding='utf8')


        # 发送消息
        response = requests.request("POST", urlsend, data=data, params=querystring)

        print(response.text)
