#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 18:59:56 2018

@author: fatdou
"""
#元类从type继承下来
def add(self, value):
    self.append(value)

class ListMetaclass(type):
    #attrs是hash表，想要加什么都可以直接添加到attrs表中,python去读这张表知道自己有哪些方法和属性
    def __new__(cls, name , bases, attrs):
#        print(cls)
#        print(name)
#        print(bases)
#        print(type(attrs))
        #attrs['add'] = lambda self, value : self.append(value)
        attrs['add'] = add
        attrs['name'] = 'Fat'
        return type.__new__(cls, name , bases, attrs)
class MyList(list, metaclass = ListMetaclass): #额外增加add方法，实际等价于append
     pass
 
mli = MyList()
mli.add(1)
mli.add(2)
mli.add(3)
print(mli)
print(mli.name) 