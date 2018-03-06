# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 23:15:13 2018

@author: yuan
"""

print((1024).to_bytes(2, byteorder = 'big'))
print((65536).to_bytes(8, byteorder = 'little'))
print((-1024).to_bytes(4, byteorder='big',signed=True))
print((-1024).to_bytes(4, byteorder='little',signed=True))
print((500).to_bytes(2, byteorder='big'))
print('%x' % 3345) 
print('%x' % 3124)

print(0xd11)
print(0xc34)

b = b'china\r\nus'
print(type(b))
s=b.decode()
print(s)
print(s.encode())