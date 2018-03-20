# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 13:14:29 2018

@author: yuan
"""

#set元素没有重复
s_a = set([1,2,2,3,4,5,6])
s_b = set([4,5,6,7,8,9])
print(s_a)
print(s_b)

#与C++的set进行区分，python set是无序的
print(5 in s_a)
print(10 in s_b)

#并集
print(s_a | s_b)
print(s_a.union(s_b ))

#交集
print(s_a & s_b)
print(s_a.intersection(s_b))

#差集 A-B:A - (A,B)的并集
print(s_a - s_b)
print(s_a.difference(s_b))

#对称差(A | B) - (A & B),把
print(s_a ^ s_b)
print(s_a.symmetric_difference(s_b))

#修改元素
s_a.add('x')
s_a.update([4,5,60,70])
print(s_a)

#删除元素,必须知道元素的值，否则无法删除
s_a.remove(60)
print(s_a)

try:
    s_a.remove(10)
except:
    print('KeyValue')
