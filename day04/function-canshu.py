#!/usr/bin/env python
# -*- coding:utf-8 -*-

#参数学习  参数是我们的函数在执行的时候索取的数据

#print len()
#报错  TypeError: len() takes exactly one argument (0 given) 缺少一个参数
'''
print len("abcd")

a="thisisatest"
print len(a)
'''

#函数中定义的ab都是形参，并没有任何实际的数值
def function1(a,b):
    if a>b:
        print a
    else:
        print b

function1(10, 20)
#对应的10,20就是我们函数的实参，是实际的数值，对应形参的a,b

#总结，形参在我们函数定义中使用，实参是在函数调用的时候使用

#参数的传递
def func(a,b):
    if a>b:
        print "前面的那个数字大"
    else:
        print "后面的数字大"
func(7,8)


#关键参数    函数定义时定义参数的值
def func1(a=1,b=2,c=3):
    print a
    print b
    print c
func1()          #输出1,2,3
func1(10)        #输出10,2,3
func1(10,11)     #输出10,11,3
func1(b=1111)    #输出1,1111,3

