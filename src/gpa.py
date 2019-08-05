#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019/7/3 17:09
# @Author  : Diralpo
# @Link    : https://github.com/Diralpo/
# @Desc    :

from cookie import *
from classes.grade import *
from src import savefile

colorList = ['black', 'aqua', 'blue', 'brown', \
    'bright_green', 'coral', 'cyan_ega', 'dark_purple', \
    'dark_red', 'gold', 'dark_yellow']
#colorList = [2, 3, 4, 6, 7, 8]
colorCnt = len(colorList)


def gpa_buaa(grade_list):
    def switch(flo):
        if flo == "优秀":
            return 4
        elif flo == "良好":
            return 3.5
        elif flo == "中等":
            return 2.8
        elif flo == "及格":
            return 1.7
        elif flo == "不及格":
            return 0
        try:
            flo = float(flo)
        except ValueError:
            flo = 0
        if flo >= 60:
            return 4 - 3 * (100 - flo) * (100 - flo) / 1600
        return 0

    a = 0.0
    b = 0.0
    for agrade in grade_list:
        b = b + agrade.xuefen
        a = a + switch(agrade.zongchengji) * agrade.xuefen
    return a / b

def cxcj(user_data):
    url = r'http://10.200.21.61:7001/ieas2.1/cjcx/queryTyQmcj'
    req = urllib.request.Request(url=url, headers=headers)
    res = opener.open(req)
    html = res.read().decode('utf-8')

    pageXnxq_from = re.findall(r'<option value="(.+?)季</option>',html)
    pageXnxq_list = []
    for astr in pageXnxq_from:
        a = astr.split("\"",1)
        pageXnxq_list.append( a[0])

    result_html = []

    for pageXnxq_str in pageXnxq_list:
        postdata={
        'pageXnxq': pageXnxq_str
        }
        postData = urllib.parse.urlencode(postdata).encode('utf-8')
        req = urllib.request.Request(url=url,data=postData ,headers=headers)
        res = opener.open(req)
        html = res.read().decode('utf-8')
        result_html.append(html)
        savefile.save_html(html,"save/gpa/{}/{}.html".format(user_data[0], pageXnxq_str))
    return result_html

def load_grade(html, grade_list):
    soup = BeautifulSoup(html, 'lxml')
    table_list = soup(class_ = 'bot_line')
    student_grade = []
    for each_data in table_list:
        tr_list = each_data.find_all('tr')
        for tr in tr_list:
            td_list = tr.find_all('td')
            student_grade_td = []
            for td in td_list:
                student_grade_td.append(td.string )
            student_grade.append(student_grade_td)

    for i in student_grade:
        if(len(i) == 15):
            try:
                astudent = Grade(i)
                grade_list.append(astudent)
            except:
                pass

def gpa(user_data):
    import xlwt
    html_list = cxcj(user_data)
    grade_list = []
    output = ""
    for html in html_list:
        load_grade(html, grade_list)
    wbk = xlwt.Workbook()
    sheet = wbk.add_sheet('sheet 1')
    i = 0
    sheet.write(i, 0, '课程名称')
    sheet.write(i, 1, '成绩')
    sheet.write(i, 2, '总成绩')
    sheet.write(i, 3, '时间')
    sheet.write(i, 4, '学分')
    sheet.write(i, 5, '课程代码')
    sheet.write(i, 6, '开课院系')
    sheet.write(i, 7, '课程性质')
    sheet.write(i, 8, '课程类别')

    sheet.col(0).width = 256 * 30
    sheet.col(5).width = 256 * 15
    sheet.col(6).width = 256 * 30
    sheet.col(8).width = 256 * 30
    pre_time = None
    t = 2
    the_style = xlwt.easyxf("font:colour {};".format(colorList[t % colorCnt]))
    #the_style = xlwt.easyxf("font:colour_index {};".format(colorList[t % colorCnt]))
    i = 1
    for agrade in grade_list:
        flag = False
        output = output + agrade.toStr()
        if pre_time == None:
            flag = True
            pre_time = agrade.xuenian
        elif pre_time != None and pre_time!=agrade.xuenian:
            flag = True
            pre_time = agrade.xuenian
        if flag:
            t += 1
            '''
            if t == 2:
                t = 4
            else:
                t = 2
            '''
            #the_style = xlwt.easyxf("font:colour_index {};".format(colorList[t % colorCnt]))
            the_style = xlwt.easyxf("font:colour {};".format(colorList[t % colorCnt]))
            # print("change", t)
        # print('t = ', t)
        sheet.write(i, 0, agrade.name, the_style)
        sheet.write(i, 1, agrade.chengji, the_style)
        sheet.write(i, 2, agrade.zongchengji, the_style)
        sheet.write(i, 3, agrade.xuenian, the_style)
        sheet.write(i, 4, agrade.xuefen, the_style)
        sheet.write(i, 5, agrade.daima, the_style)
        sheet.write(i, 6, agrade.yuanxi, the_style)
        sheet.write(i, 7, agrade.xingzhi, the_style)
        sheet.write(i, 8, agrade.leibie, the_style)

        i += 1
        print(agrade)

    wbk.save("save/gpa/{}.xls".format(user_data[0]))
    print("\n\ngpa = {}".format(gpa_buaa(grade_list)))
    output = output + "\n\ngpa = {}".format(gpa_buaa(grade_list))
    savefile.save_html(output, "save/gpa/{}/result.txt".format(user_data[0]))

