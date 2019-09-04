#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019/7/3 17:09
# @Author  : Diralpo
# @Link    : https://github.com/Diralpo/
# @Desc    :

from cookie import *

import classes
from src import signin
from src import kbcx
from src import savefile
from src import gpa


if __name__ == '__main__':
    if len(sys.argv) == 1 or (sys.argv[1] == "-h" or sys.argv[1] == "help"):
        filename = "help.txt"
        if(os.path.isfile(filename) == True):
            with open(filename , "r" ,encoding='utf-8') as in_file:
                lines = in_file.read()
                print(lines)
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

    try:
        signin.sign_in(user_data)
    except:
        sys.exit(0)

    select = int(input("请输入想进行的操作:(0：查询gpa  1：查询课表)\n"))
    if select == 0:
        gpa.gpa(user_data)
    elif select == 1:
        kbcx.kbcx(user_data)

