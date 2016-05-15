#!/usr/bin/python
# -*- coding: utf-8 -*-
#copyRight by heibanke 

import numpy as np  
import matplotlib.pyplot as plt  
    
x = np.linspace(-1,1,100)  
y = 2*np.sin(x*2.3)+0.5*x**3

y1 = y+0.5*(np.random.rand(len(x))-0.5)

A = np.vstack((x,np.ones(len(x)))).T
b = y1.reshape(y1.shape[0],1)

def projection(A,b):
    ####
    # return A*inv(AT*A)*AT*b
    ####
    AA = A.T.dot(A)
    w=np.linalg.inv(AA).dot(A.T).dot(b)
    print w
    return A.dot(w)

yw = projection(A,b)
yw.shape = (yw.shape[0],)

plt.plot(x,y,color='g',linestyle='-',marker='') 
plt.plot(x,y1,color='m',linestyle='',marker='o')
plt.plot(x,yw,color='r',linestyle='',marker='.')

plt.show()
