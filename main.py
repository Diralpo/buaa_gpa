# -*- coding: UTF-8 -*-

import io, sys

from cookie import *

import classes
from src import signin
from src import kbcx
from src import savefile
from src import gpa

'''
def init(): # 创建必备文件夹
    father_path = ["save/qiangke","save/user"]
    for path in father_path:
        isExists=os.path.exists(path)
        if not isExists:
            os.makedirs(path)
'''

if __name__ == '__main__':
    if len(sys.argv) == 1 or (sys.argv[1] == "-h" or sys.argv[1] == "help"):
        filename = "help.txt"
        if(os.path.isfile(filename) == True):
            with open(filename , "r" ,encoding='utf-8') as in_file:
                #sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')
                lines = in_file.read()
                print(lines)
                '''
            help_text = open(filename , "r" ,encoding='utf-8').read().encode('gbk')
            print(help_text)'''
        else:
            print("help file does not exist...")
        sys.exit()
    elif sys.argv[1] == "save":
        user_data = [sys.argv[2], sys.argv[3]]
        if(len(sys.argv) == 5):
            savefile.save_user(user_data, path = "save/user/{}".format(sys.argv[4]))
        else:
            savefile.save_user(user_data)
    elif sys.argv[1] == "load":
        if(len(sys.argv) == 3):
            user_data = savefile.load_user(path = "save/user/{}".format(sys.argv[2]))
        else:
            user_data = savefile.load_user()
        print("Successful reading...")
        #print(user_data)
    else:
        print("unknown command...")
        sys.exit()
    has_error = True
    while(has_error):
        try:
            signin.sign_in(user_data)
            has_error = False
        except:
            has_error = True

    select = int(input("请输入想进行的操作:(0：查询gpa  1：查询课表)\n"))
    if select == 0:
        gpa.gpa(user_data)
    elif select == 1:
        kbcx.kbcx(user_data)

