#!/usr/bin/env python
# -*- coding:utf-8 -*-

#字典的常用方法 
city_codes = {"suzhou":'0512',"beijing":'011',"shanghai":'012',"nanjing":'215'}
#获取key对应的value值
print city_codes.get('suzhou')
print city_codes.items()
print city_codes.keys()
print city_codes.values()

#删除元素
city_codes.pop('suzhou')
print city_codes

#判断对应的key指是否存在
print city_codes.has_key('beijing')