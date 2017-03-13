#!/usr/bin/env python
# -*- coding:utf-8 -*-

#属性的学习

#创建一个类
class woman():
    pass

#对类进行实例化输出对象
wandama = woman()


#查看一个实例具体有哪些属性，使用__dict__
print wandama.__dict__

#给实例wangdama添加一个属性，对应的只是baise，再次使用__dict__查看
wandama.toufa="baise"
print wandama.__dict__

#再次实例化一个对象，看对应的属性是否会进行传递
lidama = woman()
print lidama.__dict__
#属性是不会进行传递的

#查看一个实例所属类的属性
print wandama.__class__.__dict__
#对应的输出{'__module__': '__main__', '__doc__': None}

#如何费某个实例所属的类添加一个属性
wandama.__class__.xiezi="heise"
print wandama.__class__.__dict__
print lidama.__class__.__dict__ 
#这个就存在一个问题，我们wandama的属性将对应的值也传递给了lidama
#最后结论：在单独的修改某个实例属性时候，其他的属性不受影响，若修改类的属性，那么该类下所有的实例类属性都会受到影响   