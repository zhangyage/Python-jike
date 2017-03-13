#!/usr/bin/env python
# -*- coding:utf-8 -*-

#类的常用方法，不用定义直接使用
#__init__ ,构造函数
class people:
    def hi(self):
        print 8899
    def __init__(self):  #构造函数的意义在于，只要我们实例化对象，这个函数就会执行
        a="A:how are you?"
        b="B:fine,thankyou"
        print a + '\n'+b

people()  #实例化对象

#__del__,析构函数     在函数执行完成后释放函数，这个刚好和我们的构造函数相反
class friend:
    def hi(self):
        print 8899
    def __init__(self):
        print "我是构造函数__init__"
    def __del__(self):
        print "我是析构函数 ，对象生命周期结束！"

#xiaohang = friend()
#xiaohang.hi()

#friend()

friend().hi()