#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask_script import Manager
from app import app
from models import User

manager = Manager(app)

@manager.command
def hello():
    print "hello world"
    
@manager.command
def save():
    user = User(1,'jike')
    user.save()

@manager.command
def query_all():
    users = User.query_all()
    for u in users:
        print u
    
if __name__ == "__main__":
    manager.run()