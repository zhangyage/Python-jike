#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pymongo
from util.DataBaseManager import DataBaseManager
 
dataBaseManager = DataBaseManager()
print dataBaseManager.select()
rows = dataBaseManager.select()
 
for row in rows:
    print row

# connection = pymongo.MongoClient("192.168.75.129",27017)
# tdb = connection.webControl
# post_info = tdb.test
#  
# rows = post_info.find()
# for row in rows:
#     print row
