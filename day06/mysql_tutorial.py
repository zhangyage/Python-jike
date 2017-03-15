#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
演示数据的插入操作
学习常见的连接操作mysql的方法
1、官方客户端mysql-connector使用
2、第三方客户端MySQLdb
3、MySQLdb的二次封装torndb使用
'''
from __future__ import print_function

sql = "insert into ipdata (startip,endip,loacl,country) values (16777123,16777324,'电信','青海省')"
sql_tmp = "insert into ipdata (startip,endip,loacl,country) values (%s,%s,%s,%s)"
values = [(26777123,26777324,'移动','新疆省'),(26787123,26787324,'电信','云南省'),(26797123,26797324,'移动','广西省'),(29777123,29777324,'移动','四川省')]
    #定义sql语句

#实例一
#https://dev.mysql.com/downloads/connector/python/
#使用mysql-connector需要安装相关的驱动程序，linux安装mysql-client、windows安装上面连接下载的程序
'''
'''
print ('mysql-connector'.center(50,'+'))
from mysql import connector

cnx = connector.Connect(host="192.168.75.133",user="zhangyage",password="zhangyage",database="pythontest",charset="utf8")
    #创建链接
cnx.autocommit = True
db0 = cnx.cursor()
    #创建游标
print (db0.execute(sql))
print (db0.executemany(sql_tmp,values))
    #执行sql

实例二  MySQLdb
'''
'''
print ('mysql-MySQLdb'.center(50,'+'))
import MySQLdb
def connect_mysql(db_host="192.168.75.133",user="zhangyage",password="zhangyage",database="pythontest",charset="utf8"):
    conn = MySQLdb.connect(host=db_host,user=user,passwd=password,db=database,charset=charset)
    conn.autocommit(True)
    return conn.cursor()

db1 = connect_mysql()
print (db1.execute(sql),db1.lastrowid)
print (db1.executemany(sql_tmp,values),db1.lastrowid)
    #执行sql  db1.lastrowid打印最后执行的行号

'''
实例三  torndb
torndb模块是需要我们后期安装的，python -m pip install torndb
'''  
print ('mysql-torndb'.center(50,'+'))
import torndb
import simplejson as json

db2 = torndb.Connection(host="192.168.75.133",
                        user="zhangyage",
                        password="zhangyage",
                        database="pythontest",
                        charset="utf8"    
                        )
print (db2.insert(sql))
print (db2.insertmany(sql_tmp, values))
    #输出结果直接是json串，字段和对应的值到时存在的    
