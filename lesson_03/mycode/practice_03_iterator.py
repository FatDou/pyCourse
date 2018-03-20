# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 23:43:16 2018

@author: yuan
"""

from collections import Iterable
from collections import Iterator

print(isinstance([1,2,3], Iterable))

print(isinstance({},Iterable))
print(isinstance(123,Iterable))
print(isinstance('abc',Iterable))

#可迭代，不是迭代器
print(isinstance([1,2,3,4],Iterator))
print(isinstance([1,2,3,4],Iterable))

g = (x * x for x in range(10))
print(type(g))
print(isinstance(g, Iterator))
print(isinstance(g, Iterable))
for i in g:
    print(i)
    
def fib(limit):
    n, a, b = 0, 0, 1
    while n < limit:
        yield b
        a, b = b, a + b
        n += 1
    return 'done'
    
f = fib(6)
print(type(f))
print(isinstance(f, Iterator))
print(isinstance(f, Iterable))
for i in f:
    print(i)