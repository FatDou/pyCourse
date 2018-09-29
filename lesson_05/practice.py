#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 10:25:12 2018

@author: fatdou
"""
"""
#直接读入
file1 = open("test.txt")
file2 = open("output.txt", "w")

while True:
    line = file1.readline()
    s = len(line)
    file2.write(line)
    if not line:
        break
#关闭文件流
file1.close()
file2.close()


file2 = open("output.txt", "w")
for line in open("test.txt"):
    file2.write(line)

file2.close()


#文件上下文管理器
#打开文件
#用with..open自带关闭文本的功能
with open("test.txt") as f:
    data = f.read()
    print("data: " + data)

with open("output.txt", "w") as f:
    line1 = "fatdou \n"
    print(line1, file = f)

f = open("wechat.jpg", "rb")
print(f.read())
    
"""
import os
"""
print(os.name)
print(os.uname())
print(os.environ)
os.path.join(os.path.abspath('.'), 'Pictures')
print (os.path.abspath(''))
print (os.path.join(os.path.abspath('.'), 'Pictures'))
os.mkdir(os.path.join(os.path.abspath('.'), 'Pictures'))
os.path.join(os.path.abspath('.'), 'Pictures')
os.rmdir(os.path.join(os.path.abspath('.'), 'Pictures'))
os.path.join(os.path.abspath('.'), 'Pictures')
print(os.path.split(os.path.join(os.path.abspath('.'), 'output.txt')))

os.rename(os.path.join(os.path.abspath('.'), 'output.txt'), 'hi.txt')

import shutil

shutil.copyfile(os.path.join(os.path.abspath('.'),'hi.txt'), os.path.join(os.path.abspath('.'),'output.txt'))
i = 0
for x in os.listdir(os.path.join(os.path.abspath('.'))):
    if os.path.isdir(x):
        i += 1
        print(i, ' : ',x)    
 """
"""
序列化
"""
import pickle
"""
#定义一个字典
d = dict(name='思聪', age = 29, score = 80)
#通过调用pick的dumps函数进行序列化处理
str = pickle.dumps(d)
print(str)
 
#定义和创建一个file文件，设定模式为wb
f = open(os.path.join(os.path.abspath('.'), 'test2.txt'), 'wb')
 
pickle.dump(d,f)
f.close()
"""

"""
反序列化
"""
"""
#从之前序列化的test2.txt读取内容
f = open(os.path.join(os.path.abspath('.'), 'test2.txt'),'rb')
#调用Load做反序列化处理
d = pickle.load(f)
f.close()
print(d)
print('name is %s' % d['name'])
"""
"""
import json
#定义dict字典对象
d1 = dict(name = '小王', age = 20, score = 80)
#调用json的dumps函数进行json序列化处理
str = json.dumps(d1)

#调用json的loads函数进行反序列化处理
d2 = json.loads(str)

print(d2)

"""
"""
高阶函数
"""
"""
print(abs(-10))

f = abs

print(f(-10))

def add(x, y ,f):
    return f(x + y)

print(add(10,-30,abs))
"""

"""
匿名函数
"""
"""
sum = lambda arg1, arg2 : arg1 + arg2

print(sum(10,20))
"""
"""

"""
"""
from functools import reduce

l = [1,2,3,4,5]
#这个代表把list中的值，一个个放入lambda的x,y中
print(reduce(lambda x, y : x + y, l))

#x开始的时候被赋值为10，然后依次将l中的值放入lambda的x,y中；
print(reduce(lambda x, y : x + y, l ,10))

"""
"""
map
"""
"""
l = [1,2,3]
#在python3中，外面需要加一个List：
#这里加List是为了把值显示出来，不然会得到map函数
#python2没问题
new_list = list(map(lambda x : x + 1, l))
print(new_list)

#也可以把两个数组搞成一个单独的数组
l2 = [4,5,6]
new_list = list(map(lambda x, y : x + y, l, l2))
print(new_list)
"""

"""
filter

"""
#l = [100,20,24,50,110]
#new = list(filter(lambda x: x < 50, l))
#print(new)

"""
偏函数
"""
#def int2(x, base=2):
#    return int(x, base)
#
#print(int2('100'))

#import functools
#
#print(int('10000', base = 2))
#
#int2 = functools.partial(int, base = 2)
#
#print(int2('1000'))
#
#max2 = functools.partial(max, 10)
#
#print(max2(5,6,7))

"""
装饰器
"""
import logging

#def use_logging(func):
#    logging.warn("%s is running" % func.__name__)
#    func()
#
#def bar():
#    print('i am bar')
#
#use_logging(bar)

#def use_logging(func):
#    
#    def wrapper(*args, **kwargs):
#        logging.warn("%s is running" % func.__name__)
#        return func(*args)
#    return wrapper
#
#@use_logging
#def foo():
#    print("i am foo")
#
#@use_logging
#def bar():
#    print("i am bar")
#
#bar()

"""
单参数的装饰器
"""
#def use_logging(level):
#    def decorator(func):
#        def wrapper(*args, **kwargs):
#            if level == "warn":
#                logging.warn("%s is running" % func.__name__)
#            return func(*args)
#        return wrapper
#    return decorator
#
#@use_logging("warn")
#def bar():
#    print("i am bar")
#
#bar()

file = open("pima-indians-diabetes.txt")
data = []
datas = []
for line in file.readlines():
    line = line.strip('\n').split(',')
    for i in range(len(line)):
        line[i] = float(line[i])
    datas.append(line)
    


data2 = []
data1 = datas[:]


for i in range(len(datas)):
    del(data1[i][-1])
    print(data1[i])
    data2.append(datas[i][-1])
    print(data2[i])

