#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
flask学习一个简单的学习使用flask输出hello
'''
from flask import Flask
from flask import render_template
#这个是为了导入网页模板，渲染网页
from flask import url_for
#这个是为了调用图片等静态文件
from flask import request
#对应的方法是为了从前台获取数据给后台处理
from flask import redirect
#redirect是一个跳转方法，当访问首页的时候跳转到add页面

app=Flask(__name__)
@app.route('/',methods=['GET','POST'])
def index():
#    return "this is a test"
    return redirect(url_for('add'))
    

@app.route('/add',methods=['GET','POST'])
def add():
    if request.method == "POST":
        a=request.form['adder1']
        b=request.form['adder2']
        a=int(a)
        b=int(b)
        c=a+b;
        return render_template('index.html',message=str(c))
    return render_template('index.html')
#    message = "Backend message"
#    return render_template('index.html',message=message)      #网页文件需要放置在templates目录中，会自动查找

if __name__ == "__main__":
    app.run(port=8080)
