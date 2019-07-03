#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019/7/3 17:09
# @Author  : Diralpo
# @Link    : https://github.com/Diralpo/
# @Desc    :

from bs4 import BeautifulSoup

def strip_whitespace(data_list):
    result = []
    for str in data_list:
        result.append(str.strip())
    return result

class Course():
    def __init__(self, data_list):
        data_list = strip_whitespace(data_list)
        self.rwh = data_list[0]
        self.zy = data_list[1]
        self.qz = data_list[2]
        self.pageXklb = data_list[3]
        self.pageXkmkdm = data_list[4]
        self.pageKclb = data_list[5]
        self.pageXnxq = data_list[6]
        self.pageKkxiaoqu = data_list[7]
        self.pageKkyx = data_list[8]
        self.pageKcmc = data_list[9]
        self.pageYcctkc = data_list[10]

    def __str__(self):
        return "{}".format(self.rwh)
'''
    def __str__(self):
'''
