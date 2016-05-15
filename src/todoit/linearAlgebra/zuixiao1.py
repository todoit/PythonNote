#!/usr/bin/python
# -*- coding: utf-8 -*-
#copyRight by heibanke 

import numpy as np  
import matplotlib.pyplot as plt  
    
x = np.linspace(-1,1,100)  
y = 2*np.sin(x*2.3)+0.5*x**3

y1 = y+0.5*(np.random.rand(len(x))-0.5)

c = np.tile([1],100)

##################################
# 写下你的Code
#Ax^=b,求出x^,即可得到直线y=ax+b
#向量A是一个100维的向量，第一列是x1...x100,第二列是1
A = np.array([x,c]).T
#A = np.vstack((x,np.ones(len(x)))).T
#b是y1...y100
b = np.array([y1]).T
#b = y1.reshape(y1.shape[0],1)
#根据公式求x^
x_bar = (np.linalg.inv(A.T.dot(A))).dot(A.T).dot(b)

#计算直线

y2 = A.dot(x_bar)

y2.shape = (y2.shape[0],)
##################################
plt.plot(x,y,color='g',linestyle='-',marker='') 
plt.plot(x,y1,color='m',linestyle='',marker='o')

plt.plot(x,y2,color='b',linestyle='-',marker='')

# 把拟合的曲线在这里画出来

plt.show()
