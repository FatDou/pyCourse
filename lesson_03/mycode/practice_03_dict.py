# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 12:29:35 2018

@author: yuan
"""
#可以对应多个值
d = {'a' : 1, 'b': 2, 1 : 'one', 2 : 'two',3 : [1,2,3]}
print(type(dict))
print(type(d))
print(d)
#访问元素
print(d[d['a']])
print(d[1])
print(d[3])

#判断key是否存在  一个key只能对应一个value
#在内部对key进行了索引
print('c' in d)
print(3 in d)

#删除字典中元素
del(d[3])
print(d)

print(len(d))

#遍历
#1、根据Key来做遍历
for key in d:
    print(d[key])

print('...')

#2、根据key，value来做遍历
for key,value in d.items():
    print(key,value)

#3、
keys = d.keys()
print(type(keys))
print(keys)

values = d.values()
print(type(values))
print(values)

#添加元素
d[3] = [1,2,3,4]
d[3] = '1234'

print(d)
