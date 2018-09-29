#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 18:41:49 2018

@author: fatdou
"""

def  init(self, name):
    self.name = name

def say_hello(self):
    print('Hello, %s!' % self.name)
#type第二个参数的类型是tuple，如果只传一个object元素过去，python就会认为传过去的参数不正确
#，所以需要加一个,
#用type构造一个类
#Hello = type('Hello', (object,), dict(__init__ = init, hello = say_hello))
Hello = type('Hello', (object,), {'__init__' : init, 'hello' : say_hello})

'''
class Hello:
    def __init__(self, name):
        self.name = name
    def hello()
'''
h = Hello('FatDou')
h.hello( )