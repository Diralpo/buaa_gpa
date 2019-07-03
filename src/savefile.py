# -*- coding: UTF-8 -*-
from cookie import *

def save_html(file_data, path):
    father_path=os.path.abspath(os.path.dirname(path)+os.path.sep+".")
    isExists=os.path.exists(father_path)
    if not isExists:
        os.makedirs(father_path)
    f = open(path,'w', encoding='utf-8')
    f.write(file_data)
    f.close()

def access_and_save(access_url, filename, save_bool = True):
        #自定义一个请求# 先get下 lt
    req = urllib.request.Request(
        access_url
    )
    #访问该链接#
    result = opener.open(req)
    #解码返回的内容#
    result=result.read()
    #print(chardet.detect(result))
    if(save_bool == True):
        save_html(result, "save/{}".format(filename))
    return result

def save_user(user_data, path = "save/user/user.p"):
    father_path=os.path.abspath(os.path.dirname(path)+os.path.sep+".")
    isExists=os.path.exists(father_path)
    if not isExists:
        os.makedirs(father_path)

    pickle.dump(user_data, open(path , "wb" ))
    print("Successful writing...")

def load_user(path = "save/user/user.p"):
    if(os.path.isfile(path) == True):
        user_data = pickle.load(open(path , "rb" ))
        if(len(user_data)!=2):
            print("file error...")
            sys.exit()
    else:
        print("file does not exist...")
        sys.exit()
    return user_data
