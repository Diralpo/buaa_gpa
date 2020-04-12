#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019/7/3 17:09
# @Author  : Diralpo
# @Link    : https://github.com/Diralpo/
# @Desc    :

from bs4 import BeautifulSoup

def tran_Nav_Str(Navigable_String):
    return "".join(Navigable_String).strip()

class Grade():
    def __init__(self, Navigable_String):
        if len(Navigable_String) == 14:
            self.xuenian = tran_Nav_Str(Navigable_String[1])
            self.yuanxi = tran_Nav_Str(Navigable_String[2])
            self.daima = tran_Nav_Str(Navigable_String[3])
            self.name = tran_Nav_Str(Navigable_String[4])
            self.xingzhi = tran_Nav_Str(Navigable_String[5])
            self.leibie = tran_Nav_Str(Navigable_String[6])
            self.xuefen = float(tran_Nav_Str(Navigable_String[7]))
            self.zongchengji = tran_Nav_Str(Navigable_String[10])
            self.chengji = float(tran_Nav_Str(Navigable_String[11]))
        elif len(Navigable_String) == 15:
            self.xuenian = tran_Nav_Str(Navigable_String[1])
            self.yuanxi = tran_Nav_Str(Navigable_String[2])
            self.daima = tran_Nav_Str(Navigable_String[3])
            self.name = tran_Nav_Str(Navigable_String[4])
            self.xingzhi = tran_Nav_Str(Navigable_String[5])
            self.leibie = tran_Nav_Str(Navigable_String[6])
            self.zongchengji = tran_Nav_Str(Navigable_String[11])
            self.chengji = float(tran_Nav_Str(Navigable_String[12]))
            self.xuefen = float(tran_Nav_Str(Navigable_String[7]))

    def __str__(self):
        return "时间: {:<10} 学分: {:<7} 成绩: {:<7} 课程: {} ".format(
            self.xuenian, self.xuefen, self.chengji, self.name)
    def toStr(self):
        return "时间: {:<10} 学分: {:<7} 成绩: {:<7} 课程: {}\n".format(
            self.xuenian, self.xuefen, self.chengji, self.name)

    def equal(self, grade):
        if self.name == grade.name:
            #if self.name == grade.name and self.leibie == grade.leibie and self.yuanxi == grade.yuanxi:
            return True
        return False
