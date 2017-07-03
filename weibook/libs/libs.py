#!/usr/bin/env python
#coding=utf8

import urllib
import json
import types

duan = "--------------------------"  # 在控制台断行区别的

# 利用urllib2获取网络数据
def registerUrl():
    try:
        url = "https://api.douban.com/v2/book/4019736"
        data = urllib.urlopen(url).read()
        # print(eval(data))
        return eval(data)
    except Exception, e:
        print(Exception, ":", e)
