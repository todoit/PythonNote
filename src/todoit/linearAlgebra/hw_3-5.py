# coding: utf-8

import numpy as np  

#时间
years = 100

#差分方程变为矩阵乘法
A = np.array([[0.8,0.1],[0.2,0.9]]);

#初始化的人数
population_init = np.array([[3200,4000],]).T 

#求A的特征值和特征向量 
eigVals, eigVects = np.linalg.eig(A) 

#计算S和S的逆
S = eigVects
S_inv = np.linalg.inv(S) 
#计算lambda 的值
L = np.diag(eigVals) #由特征向量生成对角矩阵

population_num = S.dot(L**years).dot(S_inv).dot(population_init)

print(population_num)




