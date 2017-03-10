#!/usr/bin/env python
# -*- coding:utf-8 -*-

import pickle
lista = ["mingyue","jishi","you"]
listb = pickle.dumps(lista)
#dumps(object)将对象序列化
print listb

listc = pickle.loads(listb)
#loads(string)将对象原样恢复，并且对象类型也恢复为原来的格式
print listc