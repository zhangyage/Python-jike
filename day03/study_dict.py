#!/usr/bin/env python
# -*- coding:utf-8 -*-

#创建字典
#创建空字典
d={}
#向字典中插入第一个元素
d["name"] = "zhangyage"
print d

#第二种方法创建字典
name = ([1,"google"],[2,"facebook"])
web = dict(name)
print web

#第三种方法
w = dict(name="panyuanqing",age="23")
print w
print w["name"]

#第四种方法
book = {}.fromkeys(("python","author"),"zhang")
print book