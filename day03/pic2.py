#!/usr/bin/env python
# -*- coding:utf-8 -*-

import pickle

#dump(object,file),将对象存储到文件里面序列化
group1=("bajiu","wen","qingtian")
f1=file('1.pk1','wb')
#创建文件1.pk1并以写的方式打开
pickle.dump(group1, f1, True)
#使用dump序列化元组并存储在文件中，最后需要添加True才可以保证dump函数执行完成
f1.close()
#关闭文件
#load(object,file)将dump()存储在文件里的数据恢复
f2=file('1.pk1','rb')
#以读的方式打开文件
t=pickle.load(f2)
print t
f2.close()