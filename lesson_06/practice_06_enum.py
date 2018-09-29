#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 16:54:51 2018

@author: fatdou
"""
#
from enum import Enum

Month = Enum('Month',('Jan','Feb','Mar','Apr'))

for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)
    
jan = Month.Jan
print(jan)