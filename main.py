# -*- coding: UTF-8 -*-

import os
import sys


if __name__ == '__main__':
    if len(sys.argv) == 1 or (sys.argv[1] == "-h" or sys.argv[1] == "help"):
        filename = "data/help.txt"
        if os.path.isfile(filename) is True :
            user_data = open(filename, "r", encoding='utf-8').read()
            print(user_data)
        else:
            print("help file does not exist...")
        sys.exit()
    elif sys.argv[1] == "save":
        user_data = [sys.argv[2], sys.argv[3]]

    elif sys.argv[1] == "load":
        print("Successful reading...")
    else:
        print("unknown command...")
        sys.exit()

