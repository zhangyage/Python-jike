#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Flask
from flask import render_template

app=Flask(__name__)

@app.route('/')
def Hello():
    return "hello Python!"

@app.route('/jikexueyuan')
def Jike():
    return "hello Python,this is a jikexueyuan!"

@app.route('/jikexueyuan/<name>')
def Jikename(name):
    return name + u':你好！'

@app.route('/page/<pages>')
def page(pages):
    return u'这是第' + pages + u'页！'

@app.route('/page/<pages>/total/<totals>')
def totalpage(pages,totals):
    return u'这是第' + pages + u'页,共' + totals + u'页！'

@app.route('/templa')
def testTemp():
    title = u'测试模板'
    name = u'张亚歌'
    page = {'pages':10,'totals':50}
    return render_template('template.html',title=title,name=name,page=page)
    
if __name__ == "__main__":
    app.run(port=5000)