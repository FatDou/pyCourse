# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 12:09:53 2018

@author: yuan
"""
"""
螺旋矩阵
"""
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
        
        if(i + 1 < rows):
            #打印最右列
            for k in range(i + 1, i + rows - 1):
                result.append(matrix[k][j + columns - 1])
            #打印最下面一行
            for k in range(j + columns - 1, j, -1):
                result.append(matrix[i + rows - 1][k])
            #打印最左边这行
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

def spiral_order(matrix):
    ret = []
    rows = len(matrix)
    if rows == 0:
        return ret
    columns = len(matrix[0])
    i, j = 0, 0  # 方阵的左上角坐标
    while (rows > 0) and (columns > 0):
        for k in range(j, j + columns):  # 第一行
            ret.append(matrix[i][k])
        if rows > 1:  # 行数大于1
            for k in range(i + 1, i + rows):  # 最右列
                ret.append(matrix[k][j + columns - 1])
            if columns > 1:  # 列数大于1
                for k in range(j + columns - 2, j - 1, -1):  # 最下行
                    ret.append(matrix[i + rows - 1][k])
                for k in range(i + rows - 2, i, -1):  # 最左列
                    ret.append(matrix[k][j])
        rows -= 2
        columns -= 2
        i += 1
        j += 1
    return ret

print(spiral_order([]))
print(spiral_order([[1]]))
print(spiral_order([[1, 2], [3, 4]]))
print(spiral_order([[1,2,3],[4,5,6],[7,8,9],[10,11,12]]))

        
        
    

