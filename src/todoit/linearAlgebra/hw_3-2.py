#!/usr/bin/env python
# coding: utf-8
#copyRight by heibanke

import numpy as np  
import matplotlib.pyplot as plt  
from solutions_3 import *

# 产生一个方波(x,y)
x = np.linspace(-10,10,300) 
y=[]
for i in np.cos(x):
    if i>0:
        y.append(0)
    else:
        y.append(2)
y=np.array(y)

# write Your code, Fourier function    
plt.plot(x,y,color='g',label='origin') 
plt.plot(x,fourier(x,y,3),color='r',label='3')
plt.plot(x,fourier(x,y,8),color='b',label='8')
plt.plot(x,fourier(x,y,23),color='k',label='23')

plt.legend()
plt.axis('equal')
plt.show()
