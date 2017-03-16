#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
flask学习一个简单的学习使用flask输出hello
'''
from flask import Flask

app=Flask(__name__)

@app.route('/')
def index():
    return "Hello,Flask"

if __name__ == "__main__":
    app.run(port=8080)