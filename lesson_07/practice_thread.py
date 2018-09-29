#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 08:34:26 2018

@author: fatdou
"""


#从包中导出某个属性
from threading import Thread
import time

def my_counter():
    i = 0
    for _ in range(100000000):
        i = i + 1
    return True
"""
同时执行两个并发线程
"""
"""
def main():
    thread_array = {}
    start_time = time.time()
    for tid in range(2):
        t = Thread(target = my_counter)
        t.start()
        thread_array[tid] = t
#同时结束的操作
    for i in range(2):
        thread_array[i].join()
    end_time = time.time()
    print("Total time: {}".format(end_time - start_time))
"""

if __name__ == '__main__':
    main()
    
'''
顺序执行单线程
'''
def main():
    thread_array = {}
    start_time = time.time()
    for tid in range(2):
        t = Thread(target = my_counter)
        t.start()
        t.join()
    end_time = time.time()
    print("Total time: {}".format(end_time - start_time))
