#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 10:13:58 2018

@author: fatdou
"""

import traceback

class Student:
     #装饰器是返回一个函数，
     #生成一个新的对象叫做score,
     @property
     def score(self):
         return self.__score
     #setter是函数调用，实际调用setter这个方法是调用score这个方法。
     @score.setter
     def score(self,value):
         if not isinstance(value, int):
             raise ValueError('not int')
        
         elif(value < 0) or (value > 100):
             raise ValueError('not between 0 to 100')
         
         self.__score = value
    
    #只读属性
     @property
     def double_score(self):
         return self.__score * 2
    
s = Student()
s.score = 75
print(s.score)
             
try:
    s.score = 'abc'
except ValueError:
    traceback.print_exc()

try:
    s.score = 101
except ValueError:
    traceback.print_exc()

print('s.double_score: ', s.double_score)   
try:
    s.double_score = 150
except AttributeError:
    traceback.print_exc()