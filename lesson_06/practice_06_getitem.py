#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 12:51:13 2018

@author: fatdou
"""
class Fib:
    def __getitem__(self, n):
        a, b = 1, 1
        for i in range(n):
            a, b = b, a + b

        return a
        
f = Fib()

print(f[1])
print(f[5])
print(f[10])

