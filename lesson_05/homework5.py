#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 20:47:16 2018

@author: fatdou
"""
"""
读取文件
"""
from sklearn import svm, datasets
import numpy as np
import os
from functools import reduce

class DataSet:
    def __init__(self, name):
        
        self.name = name
    
    #读取文件内容,读到一个list中
    def readFile(self):
        file = open(self.name)
        data = []
        for line in file.readlines():
            line = line.strip('\n').split(',')
            for i in range(len(line)):
                line[i] = float(line[i])
            data.append(line)
        file.close()
        return data
    
    def generate_xy(self):
        #获得文件内容
        datas = readFile(self.name)
        #标签
        data2 = []
        #数据
        data1 = datas[:]

        for i in range(len(datas)):
        #标签
            data2.append(datas[i][-1])
        #数据
            del(data1[i][-1])
        
#        print('\n Original data looks like this: \n', data1)
#        print('\nLabels looks like this: \n', data2)
        return data1,data2
    
    def get_train_test_set(self,ratio):
        #将数据集分成训练集和测试集
        #用一个参数来区分多少分成训练集，多少分成测试机
        #首先把数据和label生成出来
        data,label = self.generate_xy()
        data = np.array(data)
        label = np.array(label)
        print(type(data))
        #计算数据长度
        n_samples = len(data)
        
        #分训练集和测试集
        n_train = n_samples * ratio
        n_train = int(n_train)
        
        X_train = data[:n_train]
        Y_train = label[:n_train]
        X_test = data[n_train:]
        Y_test = label[n_train:]
        
        #获得所有的数据
        return X_train, Y_train, X_test, Y_test
    



def main():
    data = DataSet('pima-indians-diabetes.txt')
    
    X_train, Y_train, X_test, Y_test = data.get_train_test_set(0.7)
    
    print('X_train: \n', len(X_train))
    print('Y_train: \n', len(Y_train))
    
    clf = svm.SVC()
    
    clf.fit(X_train, Y_train)
        
    clf.predict(X_test)
    
    print(clf.predict(X_test))
    
    print(X_test)
    test_point = clf.predict(X_test[12].reshape(1,-1))
    y_true = Y_test[12]
    
    print('test_point: ', test_point)
    print('y_true: ' , y_true)
    
    
    
    new_list = list(map(lambda x,y :x == y, clf.predict(X_test),Y_test ) )
    tCount = new_list.count(True)
    
    precise = lambda x,y : x / y * 100
    
    print('precise:',precise(tCount, len(new_list)),'%')

if __name__ == '__main__':
    main()