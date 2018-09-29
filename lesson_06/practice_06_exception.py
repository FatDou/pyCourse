#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 22:18:04 2018

@author: fatdou
"""
import traceback
try:
#    r = 10/0
    r = 10/1
except ZeroDivisionError as e :
    print(e)
    r = 1
else:
    print('没有异常')
finally:
    print('不管有没有异常都执行')

print(r)
 