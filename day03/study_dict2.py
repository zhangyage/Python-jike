#!/usr/bin/env python
# -*- coding:utf-8 -*-
from warnings import warn_explicit

#字典的常用方法 
city_codes = {"suzhou":'0512',"beijing":'011',"shanghai":'012',"nanjing":'215'}
#获取key对应的value值
print city_codes.get('suzhou')
print city_codes.items()
print city_codes.keys()
print city_codes.values()

#查询（添加）列表元素
print city_codes['suzhou']
#print city_codes['tianjin']
   #上面的查询方法会出现一个问题就是，当字典中有对应的Key值得时候，会正确的返回，没有的话就会报错
print city_codes.get('suzhou')
print city_codes.get('tianjin')
   #当使用get方法的时候如果对应的值存在会返回相关的values值，如果不存在则返回None
print city_codes.setdefault('suzhou')
   #返回结果0512
print city_codes.setdefault('tianjin')
   #返回结果None,并在字典中添加元素tianjin:None
print city_codes.setdefault('zhengzhou','0375')
   #返回0375并在字典中添加元素：'zhengzhou'： '0375'

#删除元素
city_codes.pop('suzhou')
print city_codes

#判断对应的key指是否存在
print city_codes.has_key('beijing')
  
print 'beijing' in city_codes
   #常用第二种方法