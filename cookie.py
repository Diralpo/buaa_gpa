#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019/7/3 17:09
# @Author  : Diralpo
# @Link    : https://github.com/Diralpo/
# @Desc    :

import os
import sys

import http.cookiejar
import urllib.request
import re
import pickle

#设置一个cookie处理器，它负责从服务器下载cookie到本地，并且在发送请求时带上本地的cookie

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
    'Referer' : 'https://sso.buaa.edu.cn/login?service=http%3A%2F%2F10.200.21.61%3A7001%2Fieas2.1%2Fwelcome'
}

class GlobalVal:
    cj = http.cookiejar.LWPCookieJar()
    cookie_support = urllib.request.HTTPCookieProcessor(cj)
    opener = urllib.request.build_opener(cookie_support, urllib.request.HTTPHandler)
    #header


    @classmethod
    def cookieReset(cls):
        cls.cj = http.cookiejar.LWPCookieJar()
        cls.cookie_support = urllib.request.HTTPCookieProcessor(cls.cj)
        cls.opener = urllib.request.build_opener(cls.cookie_support, urllib.request.HTTPHandler)
