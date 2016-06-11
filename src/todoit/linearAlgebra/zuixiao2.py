#!/usr/bin/python
# -*- coding: utf-8 -*-
#copyRight by heibanke 

import numpy as np  
import matplotlib.pyplot as plt  
from scipy.optimize import leastsq

x = np.linspace(0, -2*np.pi, 1000)
    
y = 10*np.sin(2*np.pi*0.34*x+np.pi/6)   

y1 = y + 2 * np.random.randn(len(x)) # 加入噪声之后的实验数据 

##################################
### write your code to gen A,b
m = []
for i in range(9):
    print(i)
    m.append(x**(i))
    print(m)
m.append(0.2*np.pi*x)

A = np.array(m).T
b = y1.reshape(y1.shape[0],1)


##################################

def projection(A,b):
    ####
    # return A*inv(AT*A)*AT*b
    ####
    AA = A.T.dot(A)
    w=np.linalg.inv(AA).dot(A.T).dot(b)
    print(w)
    return A.dot(w)

yw = projection(A,b)
yw.shape = (yw.shape[0],)

plt.plot(x,y,color='g',linestyle='-',marker='') 
plt.plot(x,y1,color='m',linestyle='',marker='o')
plt.plot(x,yw,color='r',linestyle='-',marker='.')

plt.show()
