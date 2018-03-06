#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 13:49:08 2018

@author: fatdou
"""

import timeit

sum_by_for = """
for d in data:
    s += d
"""

sum_by_sum = """
sum(data)
"""
sum_by_numpy_sum = """
import numpy
numpy.sum(data) 
"""

def timeit_using_list(n, loops):
    list_set = """
data = [1] * {}
s = 0
""".format(n)
    print('list result:')
    print(timeit.timeit(sum_by_for, list_set, number = loops))
    print(timeit.timeit(sum_by_sum, list_set, number = loops))
    print(timeit.timeit(sum_by_numpy_sum, list_set, number = loops))
    
def timeit_using_array(n, loops):
    array_set = """
import array 
data = array.array('L',[1] * {})
s = 0
""".format(n)
    print('array result:')
    print(timeit.timeit(sum_by_for, array_set, number = loops))
    print(timeit.timeit(sum_by_sum, array_set, number = loops))
    print(timeit.timeit(sum_by_numpy_sum, array_set, number = loops))    
    
    
def timeit_using_numpy(n, loops):
    numpy_set = """
import numpy 
data = numpy.array([1] * {})
s = 0
""".format(n)
    print('numpy result:')
    print(timeit.timeit(sum_by_for, numpy_set, number = loops))
    print(timeit.timeit(sum_by_sum, numpy_set, number = loops))
    print(timeit.timeit(sum_by_numpy_sum, numpy_set, number = loops))    
    
if __name__ == '__main__':
    timeit_using_list(3000,500)    
    timeit_using_array(3000,500)
    timeit_using_numpy(3000,500)