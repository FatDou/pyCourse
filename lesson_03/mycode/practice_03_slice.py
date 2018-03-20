# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 20:55:10 2018

@author: yuan
"""
c = []
for i in range(10):
    c.append(i)
li = c
print(type(li))

#qiepian [start:end:steps] >= start <end
print(li[2:5:1])
print(li[:4]) #[0,1,2,3]
print(li[5:]) #[5,6,7,8,9]
print(li[0:11:3])

#负值怎么处理,将-2转换成实际负数的位置
print(li[5: -2]) #[5,6,7]
print(li[9:0:-1]) #[9, 8, 7, 6, 5, 4, 3, 2, 1]
print(li[9::-1]) #[9, 8, 7, 6, 5, 4, 3, 2, 1，0]
print(li[::-2]) #[9, 8, 7, 6, 5, 4, 3, 2, 1，0]

#切片生成一个新的对象
print(li)  #还是保持原样

re_li = li[::-1]
print(re_li)