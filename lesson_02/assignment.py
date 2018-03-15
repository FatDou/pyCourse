# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 23:14:11 2018

@author: yuan
"""

"""
A．字符串按单词反转（必须保留所有空格）。' I love china!      '
转化为''      china! love I '代码如下：（可能现在有点问题）
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