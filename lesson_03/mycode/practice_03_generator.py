# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 23:19:51 2018

@author: yuan
"""

#平方表
"""
square_table = []
for i in range(10000):
    square_table.append(i * i)    
for i in range(10):
    print(square_table[i])
"""
    
#生成器写法，吧计算推迟到使用再算
square_generator = (x * x for x in range(50000))
for i in range(10):
    print(next(square_generator))

print(type(square_generator))

def fib(limit):
    n, a, b = 0, 0, 1
    while n < limit:
        yield b
        a, b = b, a + b
        n += 1
    return 'done'

import traceback
f = fib(5)
print(type(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
try:
    print(next(f))
except StopIteration:
    pass

for i in fib(5):
    print(i)