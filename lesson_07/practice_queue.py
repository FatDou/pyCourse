#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 15:37:11 2018

@author: fatdou
"""
from multiprocessing import Process,  Queue

import time

def write(q):
    for i in ['A','B','C','D','E']:
        print('Put %s to queue' % i)
        q.put(i)
        time.sleep(0.5)

def read(q):
    while True:
        v = q.get(True)
        print('get %s from queue' %v)

def main():
    q = Queue()
    pw = Process(target = write, args = (q, ))
    pr = Process(target = read, args = (q, ))
    
    pw.start()
    pr.start()
    pr.join()
    pr.terminate()

if __name__ == '__main__':
    main()

