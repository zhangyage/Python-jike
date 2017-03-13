#!/usr/bin/env python
# -*- coding:utf-8 -*-

#实现取字符串长度的功能 len()
a = "hellopython"
print len(a)
#输出结果14


#实现字符切割的功能
b = "student,youareright"
c = b.split("u")
print c
#输出结果['st', 'dent,yo', 'areright']

#自定义函数
def test():
    print "这是一个测试函数"

test()
