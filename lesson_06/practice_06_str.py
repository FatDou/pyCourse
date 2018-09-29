#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 22:24:54 2018

@author: fatdou
"""
class Myclass:
    def __init__(self, name):
        self.name  = name
    
    def __str__(self):
        return 'Hello' + self.name + '!'
print(__name__)
    
mcl = Myclass('Tom')
print(mcl)