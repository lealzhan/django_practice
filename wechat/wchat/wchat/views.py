# -*- coding: utf-8 -*-
from __future__ import unicode_literals
 
from django.http.response import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
 
from wechat_sdk import WechatBasic
from wechat_sdk.exceptions import ParseError
from wechat_sdk.messages import TextMessage
 
 
WECHAT_TOKEN = 'lingzhan'
AppID = 'wx7b307181ef0ec54a'
AppSecret = 'd7c3069f674a12c86e4c19ced0f17b49'
 
# 实例化 WechatBasic
wechat_instance = WechatBasic(
    token=WECHAT_TOKEN,
    appid=AppID,
    appsecret=AppSecret
)
 
@csrf_exempt
def weixin_main(request):
    # return HttpResponse("TEST")
    if request.method == 'GET':
        # 检验合法性
        # 从 request 中提取基本信息 (signature, timestamp, nonce, xml)
        signature = request.GET.get('signature')
        timestamp = request.GET.get('timestamp')
        nonce = request.GET.get('nonce')
 
        if not wechat_instance.check_signature(
                signature=signature, timestamp=timestamp, nonce=nonce):
            return HttpResponseBadRequest('Verify Failed')
 
        return HttpResponse(
            request.GET.get('echostr', ''), content_type="text/plain")
 
 
    # 解析本次请求的 XML 数据
    try:
        wechat_instance.parse_data(data=request.body)
    except ParseError:
        return HttpResponseBadRequest('Invalid XML Data')
 
    # 获取解析好的微信请求信息
    message = wechat_instance.get_message()
 
    # 关注事件以及不匹配时的默认回复
    response = wechat_instance.response_text(
        content = (
            '感谢您的关注！\n回复【功能】两个字查看支持的功能，还可以回复任意内容开始聊天'
            '\n【<a href="http://www.ziqiangxuetang.com">自强学堂手机版</a>】'
            ))
    if isinstance(message, TextMessage):
        # 当前会话内容
        content = message.content.strip()
        if content == '功能':
            reply_text = (
                    '目前支持的功能：\n1. 关键词后面加上【教程】两个字可以搜索教程，'
                    '比如回复 "Django 后台教程"\n'
                    '2. 回复任意词语，查天气，陪聊天，讲故事，无所不能！\n'
                    '还有更多功能正在开发中哦 ^_^\n'
                    '【<a href="http://www.ziqiangxuetang.com">自强学堂手机版</a>】'
                )
        elif content.endswith('教程'):
            reply_text = '您要找的教程如下：'
 
        response = wechat_instance.response_text(content=reply_text)
 
    return HttpResponse(response, content_type="application/xml")


# #coding=utf-8
# import hashlib
# import json
# from lxml import etree
# from django.utils.encoding import smart_str
# from django.views.decorators.csrf import csrf_exempt
# from django.http import HttpResponse
# # from auto_reply.views import auto_reply_main # 修改这里

# WEIXIN_TOKEN = 'lingzhan'

# @csrf_exempt
# def weixin_main(request):
#     # return HttpResponse("weixin  POST")
#     """
#     所有的消息都会先进入这个函数进行处理，函数包含两个功能，
#     微信接入验证是GET方法，
#     微信正常的收发消息是用POST方法。
#     """
#     if request.method == "GET":
#         signature = request.GET.get("signature", None)
#         timestamp = request.GET.get("timestamp", None)
#         nonce = request.GET.get("nonce", None)
#         echostr = request.GET.get("echostr", None)
#         token = WEIXIN_TOKEN
#         tmp_list = [token, timestamp, nonce]
#         tmp_list.sort()
#         tmp_str = "%s%s%s" % tuple(tmp_list)
#         tmp_str = hashlib.sha1(tmp_str).hexdigest()
#         if tmp_str == signature:
#             return HttpResponse(echostr)
#         else:
#             return HttpResponse("weixin  index")
#     else:
#         xml_str = smart_str(request.body)
#         request_xml = etree.fromstring(xml_str)
#         # response_xml = auto_reply_main(request_xml)# 修改这里
#         # return HttpResponse(response_xml)
#         return HttpResponse("weixin  POST")
