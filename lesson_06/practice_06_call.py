#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 12:59:52 2018

@author: fatdou
"""

class Myclass:
    def __call__(self):
        print('You can call cls() directly.')
        
cls = Myclass()

cls()

print(callable(cls))
print(callable(max))
print(callable('str'))