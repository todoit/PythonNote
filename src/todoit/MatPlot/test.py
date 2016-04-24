# -*- coding: utf-8 -*-

'''
Created on 2016年4月22日
@author: todoit
'''

import matplotlib.pyplot as plt
import numpy as np
import math 
#from math import pi
fig = plt.figure(figsize=(8,6))
ax = plt.subplot(111)
def gen_circle_point(n):
    xarr=[]
    yarr=[]
    x=y=0
    r=1
    for i in range(n):
        angle = float(i)/n*2*math.pi
        xi = x+r*np.cos(angle)
        yi = y+r*np.sin(angle)
        xarr.append(xi)  #用数组存放x坐标
        yarr.append(yi)  #用一个数组存放y坐标
     
    plt.plot(xarr,yarr,linestyle=':',color='r',marker='D')
    plt.axis('equal')  #画出圆形，限定x=y
    plt.show()
gen_circle_point(20)