#!/usr/bin/env python
# -*- coding:utf-8 -*-

import MySQLdb


def get_conn():
    host="192.168.75.133"
    port=3306
    user="zhangyage"
    password="zhangyage"
    db="jikexueyuan"
    
    conn = MySQLdb.connect(host=host,
                           user=user,
                           passwd=password,
                           db=db,
                           port=port,
                           charset="utf8")
    
    return conn

class User(object):
    def __init__(self,user_id,user_name):
        self.user_id = user_id
        self.user_name = user_name
     
    def save(self):
        conn = get_conn()
        cursor = conn.cursor()
        sql = "insert into user(user_id, user_name) VALUES(%s,%s)"
        cursor.execute(sql,(self.user_id, self.user_name))
        conn.commit()
        cursor.close()
        conn.close()
        
    @staticmethod
    def query_all():
        conn = get_conn()
        cursor = conn.cursor()
        sql = "select * from user"
        cursor.execute(sql)
        rows = cursor.fetchall()
        users = []
        for row in rows:
            user = User(row[0],row[1])
            users.append(user)    
        conn.commit()
        cursor.close()
        conn.close()
        return users
    
    def __str__(self):
        return "id:{}-name:{}".format(self.user_id,self.user_name)