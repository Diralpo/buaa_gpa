#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019/7/3 17:09
# @Author  : Diralpo
# @Link    : https://github.com/Diralpo/
# @Desc    :
#
from bs4 import BeautifulSoup

from cookie import *

def sign_in(user_data):# 首先登录账户
    # 重置全局变量
    GlobalVal.cookieReset()

    #自定义一个请求# 先get下 lt
    req = urllib.request.Request(
        'https://sso.buaa.edu.cn/login?service=http%3A%2F%2Fjwxt.buaa.edu.cn%3A7001%2Fieas2.1%2Fwelcome'
    )
    #访问该链接#
    result = GlobalVal.opener.open(req)
    #解码返回的内容#
    result=result.read().decode("utf-8")
    #找到lt
    ltItem=re.findall('<input.*?name="lt".*?value="(.*?)".*?/>',result,re.S)
    #需要POST的数据
    postdata={
        'username':user_data[0],
        'password':user_data[1],
        'lt':ltItem[0],
        'execution':'e1s1',
        '_eventId':'submit',
        'submit':'%E7%99%BB%E5%BD%95',
        'code':''
    }
    #需要给Post数据编码
    postData = urllib.parse.urlencode(postdata).encode('utf-8')
    req = urllib.request.Request(
        'https://sso.buaa.edu.cn/login?service=http%3A%2F%2Fjwxt.buaa.edu.cn%3A7001%2Fieas2.1%2Fwelcome',
        postData,
        headers
    )
    #访问该链接#
    result = GlobalVal.opener.open(req)
    the_html = result.read().decode('utf-8')
    soup = BeautifulSoup(the_html, "html.parser")
    logoutA = soup.find("a", id="logout")
    if not logoutA:
        print("存在问题，可能是账号或密码错误...\n\n")
        # print(the_html)
        return False
    return True

def logout():
    postdata={
        'Host': 'sso.buaa.edu.cn',
        'Referer': 'http://10.200.21.61:7001/ieas2.1/welcome'
    }
    #需要给Post数据编码
    postData = urllib.parse.urlencode(postdata).encode('utf-8')
    req = urllib.request.Request(
        'https://sso.buaa.edu.cn/logout',
        postData,
        headers
    )
    #访问该链接#
    result = GlobalVal.opener.open(req)
    the_html = result.read().decode('utf-8')
    #  print(the_html)
