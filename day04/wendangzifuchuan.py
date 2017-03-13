#!/usr/bin/env python
# -*- coding:utf-8 -*-

def test():
    '''这是一个测试。
    
                 测试文档字符串。'''
    print "test!"

print test.__doc__

#输出结果为： 这是一个测试。
    
 #                测试文档字符串。
 #这个作用是对我们书写的函数进行一下对应的功能解释，和书写内容的解释，记住上面的格式和相关的标点符号