#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 09:49:36 2018

@author: fatdou
"""
#创建类

class Foo:
    def bar(self):
        print('Bar')
    
    def hello(self, name):
        print('i am %s' %name)

#根据Foo创建对象
obj = Foo()
obj.bar()
obj.hello('FatDou')

#self的含义
class Foo:
    name = 'Jan'
    
    def bar(self):
        print('Bar')
    def hello(self, name):
        print('you are %s' %self.name)
        print('i am %s' %name)
        print('\n')

obj1 = Foo()
obj2 = Foo()
obj1.hello('fAT')
obj2.hello('Dou')

#构造函数
class Foo:
    def __init__(self):
        self.name = 'Jan'
    
    def hello(self, name):
        print('you are %s' %self.name)
        print('i am %s' %name)
        print('\n')

obj1 = Foo()
obj2 = Foo()
obj1.hello('fAT')
obj2.hello('Dou')

#构造函数含有参数
class Foo:
    def __init__(self, name2):
        self.name = name2
    
    def hello(self, name):
        print('you are %s' %self.name)
        print('i am %s' %name)
        print('\n')
#这里需要初始化
obj1 = Foo('Fat')
obj2 = Foo('Dou')
obj1.hello('Fat')
obj2.hello('Dou')

##访问权限
class Student:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    def print(self):
        print(self.__name)
        print(self.__age)

LiLei = Student('Lilei', '12')
LiLei.print()
        
#getter和setter方法
class Student:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    def get_name(self,name):
        return self.__name
    def get_age(self, age):
        return self.__age
    def set_age(self, age):
        self.__age  = age;
    def set_name(self, name):
        self.__name  = name;
    def print(self):
        print(self.__name)
        print(self.__age)

LiLei = Student('Lilei', '12')
LiLei.set_age('20')
LiLei.print()

#继承
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def detail(self):
        print(self.name)
        print(self.age)

class PrimaryStudent(Student):
    def lol(self):
        print('不服scala')
    
class CollegeStudent(Student):
    def __init__(self, name, age, gf):
        self.name = name
        self.age = age
        self.gf = gf
    def gf_datail(self):
        print(self.gf)

obj1 = PrimaryStudent('Fat',12)
obj1.lol()
obj1.detail()

obj2 = CollegeStudent('Dou',23,'Jing')
obj2.detail()
obj2.gf_datail()

#经典类

class D:
    def bar(self):
        print('D.bar')
class C(D):
    def bar(self):
        print('C.bar')
class B(D):
    pass
class A(B, C):
    pass

a = A()
a.bar()

#新类
class D(object):
    def bar(self):
        print('D.bar')

class C(D):
    def bar(self):
        print('C.bar')

class B(D):
    pass

class A(B,C):
    pass

a = A()
a.bar()

print(type(123))
print(type('str'))

class A:
    pass
class B(A):
    pass
class C(B):
    pass
k = A()
g = B()
y = C()

print(isinstance(y,C))
print(isinstance(y,B))
print(isinstance('a',str))

print(dir('ABC'))

