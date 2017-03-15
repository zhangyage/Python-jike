#!/usr/bin/env python
# -*- coding:utf-8 -*-

#python中的文件操作
'''
#创建文件
fc = open('file1.txt','w')
fc2 = file('file2.txt','w')

#打开文件   #打开文件和创建文件是一样的，如果在创建文件时候存在就是打开文件操作
fc = open('file1.txt','w')
fc2 = file('file2.txt','w')
'''



#测试实例，打开文件并写入内容，关闭打开为文件
content = '''测试文件内容添加
这是一个文件
这是一个测试文件
看看是否可以添加上
'''
fw = file('file2.txt','w')   #打开文件
fw.write(content)              #写入文件内容
fw.close()                     #关闭打开的文件


#读取文件内容
fr = file('file2.txt')
while True:
    line = fr.readline()
    if len(line) == 0:
        break
    print line 
fr.close() 