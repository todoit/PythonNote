#!/usr/bin/python
# -*- coding: utf-8 -*-
#copyRight by heibanke 

import numpy as np  
import matplotlib.pyplot as plt  
    
x = np.linspace(-1,1,100)  
y = ((x*x-1)**3+1)*(np.cos(x*2)+0.6*np.sin(x*1.3))

y1 = y+(np.random.rand(len(x))-0.5)

m = []
for i in range(7):
    print(i)
    m.append(x**(i))
    print(m)


A = np.array(m).T
b = y1.reshape(y1.shape[0],1)

#投影函数
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

plt.plot(x,y,color='g',linestyle='-',marker='',label=u"理想曲线") 
plt.plot(x,y1,color='m',linestyle='',marker='o',label=u"已知数据点")
plt.plot(x,yw,color='r',linestyle='-',marker='.',label=u"拟合曲线")

plt.legend()
plt.show()
