#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 17:45:50 2018

@author: fatdou
"""

"""
描述器是实现了__set__/__get__/__del__等方法
"""
class Myproperty:
    def __init__(self, fget = None, fset = None, fdel = None):
        print('__init__',fget)
        self.fget = fget
        self.fset = fset
        self.fdel = fdel
    def __get__(self, instance, cls):
        if self.fget:
            print('__get__')
            return self.fget(instance)
    
    def __set__(self, instance, value):
        if self.fset:
            print('__set__')
            self.fset(instance, value)
    
    def __fdel__(self, instance):
        if self.fdel:
            return self.fdel(instance)
    
    def getter(self, fn):
        self.fget  = fn
    def setter(self, fn):
        print('setter', fn)
        self.fset = fn
    def deler(self, fn):
        self.fdel = fn

class Student:
    @Myproperty
    def score(self):
        return self.__score
    
    @score.setter
    def set_score(self, value):
        self.__score = value

s = Student()
s.score = 95
print(s.score)
