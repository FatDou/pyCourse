# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 23:04:48 2018

@author: yuan
"""

try:
    x = 100
    y = 200
except IndentationError:
    print('IndentationError: unexpected indent')
    
#多行代码
str = 'abcd'\
            'efgh'
print(str)

#多行字符串
str = "Hello\nWorld"
print(str)
str = """Hello
World
"""
print(str)