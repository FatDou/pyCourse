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