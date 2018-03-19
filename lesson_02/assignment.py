# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 23:14:11 2018

@author: yuan
"""

"""
A．字符串按单词反转（必须保留所有空格）。' I love china!      '
转化为''      china! love I '代码如下：（可能现在有点问题）
"""
"""
import string
def Reverse(str):
    if not str:
        return None
    s = str.split(' ')
    s_1 = ""
    i = len(s) - 1
    while i >= 0:
        if not s[i]:
            s[i] = ' '
        else:
            new = s[i] + ' '
            s[i] = new
        s_1 += s[i]
        i -= 1
    return s_1
#lintcode
def reverseWords(s):
        # write your code here
        if not s:
            return ''
        s_1 = s.split(' ')
        s_2 = ""
        i = len(s_1) - 1
        while i >= 0:
            if not s_1[i]:
                s_1[i] = ' '
            else:
                new = s_1[i] + ' '
                s_1[i] = new
            s_2 += s_1[i]
            i -= 1
        print(s_2)
        s_3 = s_2.lstrip()
        return s_3

s = 'the sky is blue   '
print(reverseWords(s))
s = '   blue is sky the'
print(s.lstrip())
"""

"""
打印100000以内的所有素数（筛法求素数）
"""
import math
def is_prime_num(number):
    if((number == 2) or (number == 3)):
        return True
    elif(((number % 6) != 1) and ((number % 6) != 5)):
        return False
    n_1 = math.floor(math.sqrt(number))
    for i in range(5, n_1 + 1, 6) :
        if ((number % i == 0) or (number % (i + 2) == 0)):
            return False
    return True
def print_prime_num(number):
    for i in range(2,number + 1):
        if is_prime_num(i):
            print(i)
        else:
            continue
            

print(is_prime_num(2))
print_prime_num(2)

"""
自己实现一个函数支持可变参数
"""
def test_1(name ,*arg):
    print(type(arg))
    print(arg)

def test_2(name, **args):
    print(type(args))
    print(args)

def test_3(*args):
    print(*args)
    
test_1('Tom', 1,2,3,4,5)
test_2('Tom',x = 0, y = 0)
test_3('x = ', 1, 'y = ','2' )
    
"""
实现函数解决hanoi塔问题
"""
def hanoi(n, a, b, c):
    if (n == 1):
        print('plate no.',1 , ' src: ',a, '-> dst: ',b)
    else:
        hanoi(n - 1, a, c, b)
        print('plate no.',n , ' src: ',a, '-> dst: ',b)
        hanoi(n - 1, c, b, a)

hanoi(3,'A','B','C')

"""
实现一个sort函数，通过参数指定比较函数用来实现按不同顺序进行排序。
主要就用了冒泡排序，默认从小到大，如果指定比较参数就从大到小
"""
def BubbleSort(nums, size, desc = None):
    for i in range(1, size, 1):
        for j in range(0, size - 1, 1):
            if not desc:
                if (nums[j] > nums[j + 1]):
                    """
                    tmp = nums[j]
                    nums[j] = nums[j + 1] 
                    nums[j + 1] = tmp
                    """
                    nums[j],nums[j + 1] = nums[j + 1], nums[j]
                else:
                    continue
            else:
                (nums[j], nums[j + 1]) = desc(nums[j], nums[j + 1])
    print(nums)

def desc(x, y):
    if (x < y):
        return y,x
    else:
        return x, y
        
BubbleSort([3,2,5,4,1],5, desc)
