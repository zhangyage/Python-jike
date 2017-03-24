#!/usr/bin/env python
# -*- coding:utf-8 -*-

import pymongo

connection = pymongo.MongoClient("192.168.75.129",27017) #创建链接
tdb = connection.jikexueyuan       #jikexueyuan创建的数据库就叫jikexueyuan
post_info = tdb.test

person = {'name':u'zhang','age':5,'skill':'Python'}
god = {'name':u'玉皇大帝','age':36000,'skill':'createanything','other':u'王母娘娘不是他的老婆'}
godslaver = {'name':u'悟空','age':1000,'skill':'72变','other':u'三大白骨精'}

post_info.insert(person)          #插入数据
post_info.insert(god)             #插入数据
post_info.insert(godslaver)       #插入数据
#post_info.remove({'name':u'zhang'})  #移除某个数据
result = post_info.find()             #获取结果

for i in result:                      #遍历打印结果
    print i
