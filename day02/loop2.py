#!/usr/bin/env python
# -*- coding:utf-8 -*-

a= 1
while a<7:
    a = a+1
    if a==4:
        continue
    for i in range(7,10):
        if i==9:
            continue
        print i