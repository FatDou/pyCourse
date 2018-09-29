#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 20:17:28 2018

@author: fatdou
"""

from multiprocessing import Pool
import time

def f(x):
    print(x*x) 
    time.sleep(3)
    return x*x

if __name__ == '__main__':
    '''
    定义启动的进程数量
    '''
    pool = Pool(processes = 5)
    res_list = []
    
    for i in range(10):
        '''
        以异步并行的方式启动进程，如果要同步等待的方式，可以在每次启动进程之后
        调用res.get()方法，也可以使用Pool.apply
        '''
        res = pool.apply_async(f,[i,])
        print('-------:',i)
        res_list.append(res)
    pool.close() 
    #强制等待所有进程执行完毕
    pool.join()
    for r in res_list:
        print("result", (r.get(timeout = 5)))