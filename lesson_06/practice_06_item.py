#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 22:42:13 2018

@author: fatdou
"""

class Fib100:
    def __init__(self):
        self.__1, self.__2 = 0,1
        
    def __iter__(self):
        return self
    
    def __next__(self):
        self.__1, self.__2 = self.__2, self.__1 + self.__2
        if self.__1 > 100:
            raise StopIteration()
        return self.__1
for i in Fib100():
    print(i)
