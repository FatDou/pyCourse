# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 09:35:27 2018

@author: yuan
"""
"""
class Myclass(object):
    pass

print(type(Myclass))
my_class = Myclass()
print(type(my_class))
"""
"""
x = 100
x = 123.45
x = 'abc'
print (x)

try:
    print(x)
except NameError:
    print("NameError, x is not be defined.")
"""
""" 
import string

str1 = 'abc'
str2 = 'b'
pos = str2.index(str1)
print(pos)
"""

import string
"""
#字符串不可以被修改
str = "    abc    efg   "
#返回的是新字符串
#去除空格
print(str.strip())
print(str.lstrip())
print(str.rstrip())

s1 = 'abc'
s2 = 'def'
print(s1+"\n"+s2)

#大小写
s = 'abc def'
print(s.upper())
print(s.lower())
print(s.capitalize())

#位置和比较
s_1 = 'abcdefd'
s_2 = 'abdeffxx'
print(s_1.index('bcd'))
try:
    print(s_2.index('bcd'))
except ValueError:
    pass
#在python3中，cmp函数被移除
print(s_1 == s_2)
print(s_1 < s_2)
print(s_1 > s_2)

print(len(s_1))

s_1 = ''
if s_1 is None:
    print('None')
else:
    print('Not None')

if not s_1:
    print('Empty')

#分割和连接
s_1 = 'abc,efg,hig'
splitted = s_1.split(',')
print(splitted)
print(type(splitted))
"""

#s = 
"""abc
def
ghi
efg"""
"""
s1 = s.split('\n')
s2 = s.splitlines()
print(s1)
print(s2)

s = ['abc', 'def', 'ghi', 'efg']
print(' '.join(s))
print(','.join(s))

s = 'abcdefg'
print(s.endswith('abc'))

s = '123bnum'
print(s.isalnum())

#字符串到数字
print(int('1234'))
print(float('1234.45'))
print(int('fff',16))

s = 'abcdefg'
l = list(s)
print(l)
"""
"""
a = 100
b = 200
c = 300
if c == a:
    print(a)
elif c == b:
    print(b)
else:
    print(c)
    
#None 的判断
x = None
if x is None:
    print('None')
else:
    print('Not None')
    
#
for i in range(0, 30, 5):
    print(i)
    
for i in range(0, 100):
    if (i < 10):
        pass
    elif(i < 30):
        continue
    elif(i < 35):
        print(i)
    else:
        break
        """
"""
def function(arg1, arg2):
    print(arg1, arg2)
    return arg1+arg2

r = function(1,2)
print(type(r))
print(r)

def fun(x,y=500):
    print('x=', x)
    print('y=', y)
    return x + y

print(fun(100))
print(fun( y = 100, x = 600))
print(fun(x = 100))

def func(p):
    print('x = ', p['x'])
    print('y = ', p['y'])
    return p['x'] + p['y c']
print(func({'x' : 100, 'y': 600}))
"""
#可变参数,* 告诉Python处理name后所有参数，把参数放到数组中去
def func(name, *number):
    print(type(number))
    print(number) 
    return 'Done'
#tuple->元组 《=》只读数组
func('Tome',1,2,3,4,'abc')
func('Tome',[1,2,3,4])
func('Tome',{'x':3,'y':4})

def my_print(*args):
    print(args)

my_print(1,2,3,4,'a','b')

def func(name, **kvs): #** means key/values
    print(name)
    print(type(kvs))
    print(kvs)

func('Tome',china = 'Beijing', uk = 'Lodon')

def func(a,b,c,*,china,uk):
    print(china,uk)

func(1,2,3,china='BJ',uk='Lodon')

def func(a, b, c = 0, *args, **kvs):
    print(a, b, c)
    print(args)
    print(kvs)
func(1,2)
func(1,2,3)
func(1,2,3,'a','b')
func(1,2,3,'a','b',x=0,y=1)
func(1,2,3,*('a','b'),**{'x':0,'y':1})

def my_print(*args):
    print(*args)

my_print('x = ', 1, 'y = ', 2 )

def my_sum(i):
    if i < 0:
        raise ValueError
    elif i <= 1:
        return i
    else:
        return i + my_sum(i - 1)
print(my_sum(5))

#f(n) = f(n - 1) + f(n - 2)
def fib(n):
    if n < 1:
        raise ValueError
    elif n <= 2:
        return 1
    else:
        return fib(n-1) + fib(n - 2)

def hanoi(n, A, B, C):
    if n == 1:
        print(A + '->' + B)
    else:
        hanoi(n - 1, A, C, B)
        print(A + '->' + B)
        hanoi(n - 1, C, A, B)
        
hanoi(4,'a','b','c')

def cmp(x, y, cp = None):
    if not cp:
        if x > y:
            return 1
        elif x < y:
            return -1
        else:
            return 0
    else:
        return cp(x,y)

def my_cp(x,y):
    if x < y:
        return -1
    elif x > y:
        return 1
    else:
        return 0
print(cmp(1,2))
print(cmp(1,2,my_cp))
print(cmp(1,2,my_cp))