#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
练习使用flask-bootstarp插件美化模板网页

链接的文件是template2.html文件，如果你先定义内容可以在{% block content %}添加你需要的内容，
可以访问http://v3.bootcss.com/css/获取模板内容
'''

from flask import Flask
from flask import render_template
from flask_bootstrap import Bootstrap


app=Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def Templa():
    name = 'zhangyage'
    return render_template('template2.html',name=name)

if __name__ == '__main__':
    app.run()        #默认启动端口是5000
    #app.run(port=9000)