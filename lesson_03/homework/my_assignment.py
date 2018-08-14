# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 12:09:53 2018

@author: yuan
"""
"""
螺旋矩阵
这个需要注意一下，打印的下标
"""

def spiral_matrix(matrix):
    result = []
    #行的长度
    rows = len(matrix)
    if (rows == 0):
        return result
    #列的长度
    columns = len(matrix[0])
    i = j = 0
    while(rows > 0 and columns > 0):
        #打印第一行,j的最大值为j+colums(当前剩下的列数)
        for k in range(j, j + columns):
            result.append(matrix[i][k])
        
        if(rows > 1):
            #打印最右列
            for k in range(i + 1, i + rows):
                result.append(matrix[k][j + columns - 1])
            #打印最下面一行
            if columns > 1:
                #打印最下面一行，要从倒数第二个数开始打印
                for k in range(j + columns - 2, j, -1):
                    result.append(matrix[i + rows - 1][k])
                #打印最左边这列，要考虑上一行的最左边那个元素
                for k in range(i + rows - 1, i, -1):
                    result.append(matrix[k][j])
            
        
        rows -= 2
        columns -= 2
        
        i += 1
        j += 1
    
    return result

print(spiral_matrix([]))
print(spiral_matrix([[1,2,3]]))
print(spiral_matrix([[1,2,3],[4,5,6],[7,8,9]]))
print(spiral_matrix([[1,2,3],[4,5,6],[7,8,9],[10,11,12]]))
print(spiral_matrix([[1,2],[3,4],[5,6],[7,8],[9,10],[11,12]]))
        
    
"""

"""


