#!/usr/bin/env python
# -*- coding:utf-8 -*-

import MySQLdb

#链接数据库
conn = MySQLdb.connect("192.168.75.133","zhangyage","zhangyage","test")

#创建游标执行数据库操作
cur = conn.cursor()

#sql语句
#添加用户
def addUser(username,password):
    sql = "insert into user (username,password) values('%s','%s')" %(username,password)
    cur.execute(sql)
    conn.commit()
    conn.close()

#判断用户是否是否存在
def isExisted(username,password):
    sql = "select * from user where username='%s' and password='%s'" %(username,password)
    cur.execute(sql)
    result=cur.fetchall()
    if(len(result)==0):
        return False
    else:
        return True