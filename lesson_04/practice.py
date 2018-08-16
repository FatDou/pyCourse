#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 17:46:10 2018

@author: fatdou
"""

from sklearn import svm,datasets

class Dataset:
    #创建一个dataset的类，这个类会帮我们下载相关的数据集，
    #并为我们分好类x,y
    def __init__(self, name):
        #告诉类，需要哪一个数据集
        #有两个选择，一个是'iris'，一个是'digits'
        self.name = name
    
    def download_data(self):
        #从sklearn的自带集中下载我们指定的数据集
        if self.name == 'iris':
            #sklearn自带的数据集下载方法
            self.downloaded_data = datasets.load_iris()
        elif self.name == 'digits':
            self.downloaded_data = datasets.load_digits()
        else:
            #如果不是需要的数据集，则报错
            print('Dataset Error: No named datasets')
    
    def generate_xy(self):
        #通过这个过程把我们的数据集分为原始数据以及他们的label
        #先下载数据集
        self.download_data()
        x = self.downloaded_data.data
        y = self.downloaded_data.target
        
        print('\n Original data looks like this: \n', x)
        print('\nLabels looks like this: \n', y)
        return x,y
    
    def get_train_test_set(self, ratio):
        #这里把数据集分为训练集和测试集
        #一个参数告知我们，以多少比例来分训练集和测试集
        #首先，将XY给generateCHULAI 
        x,y = self.generate_xy()
        #计算数据的长度
        n_samples = len(x)
        
        #分训练集和测试集
        n_train = n_samples * ratio
        n_train = int(n_train)
        
        X_train = x[:n_train]
        Y_train = y[:n_train]
        X_test = x[n_train:]
        Y_test = y[n_train:]
        
        #得到所有需要的数据
        return X_train,Y_train,X_test,Y_test
    
#在main函数中调用我们的类
def main():
    data = Dataset('digits')
    
    X_train,Y_train,X_test,Y_test = data.get_train_test_set(0.7)
    
    print('X_train: \n', X_train)
    print('Y_train: \n', Y_train)
    
    clf = svm.SVC()
    
    clf.fit(X_train, Y_train)
    
    print('clf: \n', clf)
    print('clf.fit: \n', clf.fit(X_train, Y_train))
    
    test_point = X_test[12]
    y_true = Y_test[12]
    
    print('test_point: ', test_point)
    print('y_true: ' , y_true)
    
    
    #print(help(clf.predict))
    #clf.predict(X_test)
    #reshape函数会根据另一个参数的维度计算出数组的另外一个shape属性值
    #shape代表这个矩阵是n*m的矩阵(4,4)
    #pridict不能只放一个单独的数组值~~
    clf.predict(test_point.reshape(1,-1))
    
    #print('clf.predict: \n',clf.predict(X_test))
    print('clf.predict(test_point): \n',clf.predict(test_point.reshape(1,-1)))
    print ('Y_test: ', Y_test)
if __name__ == '__main__':
    main()    