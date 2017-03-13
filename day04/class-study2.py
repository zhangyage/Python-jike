#!/usr/bin/env python
# -*- coding:utf-8 -*-

#方法的学习

#创建类
class god:
    def a(self): #定义方法  这里的self是必须的，所有的方法，第一个参数必须是self,代表所有的实例可以共享他，不具备其他任何意义
        print "所有人明天必须唱一首歌！"

zongguan=god()  #实例化对象
zongguan.a()    #使用方法，方法的调用必须通过方法调用，类是不可以直接调用方法的，不能使用抽象的类调用方法必须使用具体的实例调用方法

god().a()       #god() 这个如果（）就不在是类了，这个已经实例化了


#隐藏方法和隐藏属性
class school:
    def __jiaoxuefangfa(self):  #添加__就是隐藏方法了
        print "你可以看到吗?"

school().__jiaoxuefangfa()
#报错：    school().__jiaoxuefangfa()
#      AttributeError: school instance has no attribute '__jiaoxuefangfa'
#隐藏方法是不能在外部直接调用的