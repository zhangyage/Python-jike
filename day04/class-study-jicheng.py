#!/usr/bin/env python
# -*- coding:utf-8 -*-

#继承
class fuqin:
    def shufa(self):
        print"我会书法！"
        
class daerzi(fuqin):#继承父亲书法，但是自己开发新功能能吃
    def eat(self):
        print"我还很能吃"
        
class xiaoerzi(fuqin):
    def noeat(self):
        print"我不能吃！"
        
daerzi = daerzi()
daerzi.eat()
daerzi.shufa()

xiaoerzi = xiaoerzi()
xiaoerzi.noeat()
xiaoerzi.shufa()


print "+++++++++++++++++++++++++"

#多继承
class muniu:
    def chicao(self):
        print "我会吃草！"

class gongniu:
    def benpao(self):
        print "我会奔跑！"
        
class daniu(muniu,gongniu):#多继承
    pass

class xiaoniu(muniu): #单继承
    pass

daniu = daniu()
daniu.benpao()
daniu.chicao()


xiaoniu = xiaoniu()
xiaoniu.chicao()
#小牛没有继承父亲奔跑的功能，就没有对应的功能


#继承冲突，多个父类中有相同的方法，导致冲突
#多个父类时候，先继承的优先