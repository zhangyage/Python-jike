import pymongo

class DataBaseManager(object):
    def __init__(self):
        connection = pymongo.MongoClient("192.168.75.129",27017)
        tdb = connection.webControl
        self.post_info = tdb.test

    def insert(self, info):
        self.post_info.insert(info)
    
    def select(self):
        return self.post_info.find()