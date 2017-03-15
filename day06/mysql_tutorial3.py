#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
学习常见的连接操作mysql的方法
1、官方客户端mysql-connector使用
2、第三方客户端MySQLdb
3、MySQLdb的二次封装torndb使用
'''
from __future__ import print_function

sql = ('select * from ipdata limit 10')
    #定义sql语句
'''
#实例一
#https://dev.mysql.com/downloads/connector/python/
#使用mysql-connector需要安装相关的驱动程序，linux安装mysql-client、windows安装上面连接下载的程序
'''
print ('mysql-connector'.center(50,'+'))
from mysql import connector

cnx = connector.Connect(host="192.168.75.133",user="zhangyage",password="zhangyage",database="pythontest",charset="utf8")
    #创建链接
db0 = cnx.cursor()
    #创建游标
db0.execute(sql)
    #执行sql
for row in db0:
    print(*row)
    #print(row)
    #遍历结果         可以使用上面的两种方法输出，但是使用第一种是必须导入python的打印函数  from __future__ import print_function

'''
实例二  MySQLdb
'''
print ('mysql-MySQLdb'.center(50,'+'))
import MySQLdb
def connect_mysql(db_host="192.168.75.133",user="zhangyage",password="zhangyage",database="pythontest",charset="utf8"):
    conn = MySQLdb.connect(host=db_host,user=user,passwd=password,db=database,charset=charset)
    conn.autocommit(True)
    return conn.cursor()

db1 = connect_mysql()
db1.execute(sql)
for row in db1:
    print(*row)
    

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
rows = db2.query(sql)
for row in rows:
    print(json.dumps(row,ensure_ascii=False))
    #输出结果直接是json串，字段和对应的值到时存在的

'''    
#torndb2   get（）方法有一个特点就是在每次只能到处异常数据，多行数据时候会自动报错
row3 = db2.get(sql)
for row in rows:
    print(json.dumps(row,ensure_ascii=False))
#raise Exception("Multiple rows returned for Database.get() query")
'''
#get（）正确使用方法：
print ('mysql-torndb.get()'.center(50,'+'))
row3 = db2.get('select * from ipdata limit 1')
print(json.dumps(row,ensure_ascii=False))
 