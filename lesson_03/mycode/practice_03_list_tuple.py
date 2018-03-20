# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 08:56:59 2018

@author: yuan
"""
li = [1, 2, 3, '456', [1,2,3], {1:'one', 2: 'two'}]
print(type(list))
print(type(li))

print(li[0])
print(li[3])

#负数索引
print(li[-1])
print(li[-2])

#查找元素的位置
print(li.index('456'))
print(li.index([1,2,3]))
try:
    print(li.index(-1))
except:
    print('ValueError') 

#添加元素
l_a = [1,2,3]
l_a.append(4)
l_a.append(5)
l_b = [6,7,8]
l_a.extend(l_b)
print(l_a)

#若用append
l_a.append(l_b)
print(l_a)

#自己实现的extend
def my_extend(li, n_li):
    for i in len(n_li):
        li.append(i)

#遍历数组
for i in l_a:
    print(i)
    
for i in range(len(l_a)):
    print(l_a[i])
    
#删除
del(l_a[1])
print(l_a)
l_a.pop(-1)
print(l_a)

#判断容器是否为空
l_a = []
if not l_a:
    print('Empty')
if l_a is None:
    print('None')
if len(l_a) == 0:
    print('Empty')
    
#tuple
t = (1,2,3,'456')
print(type(t))
for i in t:
    print(i)
    
"""
给定一个数，找到数组中两个数的和等于这个数
"""
def two_sum(numbers, target):
    for i in range(len(numbers) - 1):
        for j in range(i + 1,len(numbers)):
            if (numbers[i] + numbers[j] == target):
                return i,j
            else:
                continue
    return -1,-1

list = two_sum([1,2,3,4,5,6], 10)
print(type(list))
print(list)