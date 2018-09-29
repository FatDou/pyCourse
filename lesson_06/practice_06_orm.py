#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 19:58:28 2018

@author: fatdou
"""
class Field:
    #Field代表列的名字和列的类型
    def __init__(self, name, col_type):
        self.name = name
        self.col_type = col_type

#Int的数据类型为int
class IntegerField(Field):
    def __init__(self, name):
        #调用父类的构造函数
        super(IntegerField, self).__init__(name, 'integer')
#String的数据类型为varchar 
class StringField(Field):
    #super  调用父类的构造函数
    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(1024)')

class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)
        
        print('Model name: %s' % name)
#        mapping记录的是数据库每个列的信息 
        mappings = {}
        for k, v in attrs.items():
             if isinstance(v, Field):
                 print('Field name: %s' % k)
                 #v是IntegerField或者StringField
                 mappings[k] = v
        for k in mappings.keys():
            attrs.pop(k)
        attrs['__mappings__'] = mappings
        attrs['__table__'] =  name
        print(attrs['__mappings__'])
        #建一个新类，一定有mapping和table的属性
        return type.__new__(cls, name, bases, attrs)
 
class Model(dict, metaclass = ModelMetaclass):
    def __init__(self, **kvs):
        super (Model, self).__init__(**kvs)
        
    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            return AttributeError("'Model object has no attribute '%s''" % key)
    
    def __setattr__(self, key, value):
        print('key: ', key)
        print('value:', value)
        self[key] = value
    
    def save(self):
        fields = []
        params = []
        args = []
#        k代表列名，v就是Field类型
        for  k,v in self.__mappings__.items():
            print('v.name: ', v.name)
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        sql = 'insert into %s(%s) values(%s)'% (self.__table__, ','.join(fields),','.join(params))
        print('sql: ',sql)
        print('args', args)

#数据库表的名字
class User(Model):
    #列的名字 
    #列的类型
    id = IntegerField('id')
    name = StringField('name')

u = User()
u.id = 100
u.name = 'Fat'

u.save()