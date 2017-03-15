#!/usr/bin/env python
# -*- coding:utf-8 -*-

from pymongo import MongoClient


mc = MongoClient("192.168.75.129",27017) #创建链接

db = mc.users                            #连接对应的数据集合

db.user.save({"name":"zpan","age":21})   #添加一个元素

c=db.user.find()                         #获取数据操作

for i in c:
    print(i)
    
mc.close()
#关闭连接