#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 23:22:04 2018

@author: fatdou
"""
from multiprocessing import Process
import os
import time
'''
print ('Process (%s) start...' % os.getpid())

pid = os.fork()

if pid == 0:
    print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
    print('I (%s) just created a child process (%s).' % (os.getpid(), pid))
else:
    print('I (%s) just created a child process (%s).' % (os.getpid(), pid))
'''
def f(n):
    time.sleep(1)
    print(n * n)

if __name__ == '__main__':
    start_time = time.time()
    for i in range(10):
        #target是要执行的函数
        #args是要传入的参数
        p = Process(target = f, args = [i,])
        p.start()
#        p.join()
    end_time = time.time()
    print('cost time %s' %(end_time - start_time))