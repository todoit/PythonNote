#!/usr/bin/env python
# coding: utf-8
#copyRight by heibanke

import numpy as np  
import time

# for hw_3-1
"""
两个向量a=[1,2,3],b=[1,1,1]
如何在a,b的平面上找到一个向量和a垂直。
"""
# for hw_3-2
def fourier(x,y,n):
    m = []
    for i in xrange(n):
        m.append(np.cos(x*i+x))
        m.append(np.sin(x*i+x))

    mx = np.mat(m).T

    y2 = y.reshape(y.shape[0],1)-np.mean(y)

    w=np.linalg.inv(mx.T*mx)*mx.T*y2

    yw = np.array(mx*w)+np.mean(y)
    yw.shape = (yw.shape[0],)
    return yw
  
    
# for hw_3-3
from matplotlib import pyplot as plt
import matplotlib.animation as animation

def eigshow(A):
    w=np.linspace(0,2*np.pi,100)
    x=np.array([np.cos(w),np.sin(w)])
    ax = A.dot(x)
    
    def update(num):
        s1.set_data(x[:, 0:num])
        s2.set_data(ax[:, 0:num])
        return s1,s2

    fig1 = plt.figure()

    s1, = plt.plot([], [], 'ro')
    s2, = plt.plot([], [], 'bo')
    plt.xlim(-4, 4)
    plt.ylim(-4, 4)
    plt.xlabel('x')
    plt.title('Animation2')

    line_ani = animation.FuncAnimation(fig1, update, 100,
                                       interval=50, blit=False, repeat=False)
                                       
    plt.show()

"""
########################################################
#   下节课介绍内容
#
#
#
#
#
#
# for hw_3-4    
"""