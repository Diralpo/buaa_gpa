# -*- coding: UTF-8 -*-

from cookie import *
from src import savefile

def kbcx(user_data):
    url = r'http://10.200.21.61:7001/ieas2.1/kbcx/queryGrkb'
    req = urllib.request.Request(url=url, headers=headers)
    res = opener.open(req)

    html = res.read().decode('utf-8')
    filename = re.findall(r'学期(.+?)课表',html )[0]

    savefile.save_html(html, "save/{}课表.html".format(filename))
    print( filename )
