#!/usr/bin/env python
# -*- coding:utf-8 -*-

#练习mysql链接操作            结束用户的输入添加数据库中，进行展现

import MySQLdb

#链接数据库
conn = MySQLdb.connect("192.168.75.133","zhangyage","zhangyage","test")

#创建游标执行数据库操作
cur = conn.cursor()

#sql语句
sql = "select * from student"

name = raw_input("请输入你的名字：")
#插入内容
inser_sql = "insert into student (name) values ('%s')" %(name)
cur.execute(inser_sql)
conn.commit()
#向数据库提交内容保证数据的一致性
#执行
cur.execute(sql)

#获取结果
result=cur.fetchall()
#获取的结果是以元组的形式存放的

#遍历结果
for row in result:
    print row[0]
    print row[1]
    
conn.close()
#关闭链接