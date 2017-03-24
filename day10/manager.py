#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
使用flask-Script工具导入相关插件，调用外部脚本
'''

from flask_script import Manager
from app import app

manager = Manager(app)

@manager.command
def hello():
    print "Hello Python-Script"
#在命令行中执行python manager.py hello 可以调出Hello Python-Script
    
@manager.option('-m','--msg',dest='msg_val',default='world')
def hello_world(msg_val):
    print 'hello  ' +msg_val
#在命令行中执行python manager.py hello_world 可以调出hello world  执行python manager.py hello_world -m Python 可以调出hello Python(-m是支持参数传递的)

if __name__ == "__main__":
    manager.run()