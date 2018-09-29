#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 09:31:17 2018

@author: fatdou
"""
#做异常处理
import traceback

from types import MethodType

class Myclass(object):
    __slots__ = ['name', 'set_name']

def set_name(self, name):
    self.name  = name

cls = Myclass()
cls.name = 'Tom'
#添加方法
cls.set_name = MethodType(set_name, cls)
cls.set_name('Jerry') 
print(cls.name)
try:    
    cls.age = 30
except AttributeError:
    traceback.print_exc()
    
class ExtMyclass(Myclass):
    pass

ext_cls = ExtMyclass()
ext_cls.age = 30
print(ext_cls.age)