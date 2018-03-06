#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 09:46:42 2018

@author: fatdou
"""

import requests
import xml.etree.ElementTree as ET

from xml.parsers.expat import ParserCreate

#Sax处理XML
class DefaultSaxHandler(object):
    def __init__(self, provinces):
        self.provinces = provinces
    
    def start_element(self, name, attrs):
        if name != 'map':
            name = attrs['title']
            number = attrs['href']
            self.provinces.append((name, number))
    
    #市区的名称和
    def end_element(self, name):
        pass
    
    def char_data(self, text):
        pass
    
def get_provinces(url):
    #页面抓取
    content = requests.get(url).content.decode('gb2312')
    #抓感兴趣的内容，\"就是转义字符，为了用”号
    start = content.find('<map name=\"map_86\" id=\"map_86\">')
    end = content.find('</map>')
    #做数据切断，把需要的内容提取出来.strip把空格去掉
    content = content[start:end + len('</map>')].strip()
    print(content)
    provinces = []
    handler = DefaultSaxHandler(provinces)
    parser = ParserCreate()
    parser.StartElementHandler = handler.start_element
    parser.EndElementHandler = handler.end_element
    parser.CharacterDataHandler = handler.char_data
    parser.Parse(content)
    return provinces
    
provinces = get_provinces('http://www.ip138.com/post')
print(provinces)
        