# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 23:00:28 2018

@author: yuan
"""

li = []
for i in range(10):
    li.append(i)
    
li = [0] * 10
print(li)

li = [1] * 10
print(li)

#取20前面的偶数放进数组中
li = [i * 2 for i in range(10)]
print(li)

#二维数组
#这里*3，做的引用，把这一行引用了3次。做的浅拷贝
"""
li_2d = [[0] * 3] * 3
print(li_2d)
li_2d[0][0] = 1
print(li_2d)
"""
#做深拷贝
li_2d = [[0] * 3 for i in range(3)]
print(li_2d)

li_2d[0][0] = 100
print(li_2d)

s = [x for x in range(10) if x % 2 == 0]
print(s)
#判断每个数是不是偶数
d = {x : x % 2 == 0 for x in range(10)}
print(d)