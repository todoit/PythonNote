#!/usr/bin/python
# -*- coding: utf-8 -*
# Copy Right by heibanke

import numpy as np
from matplotlib import pyplot as plt

A=np.array([[-0.2,-1],[1.1,0.5]])
U,s,V=np.linalg.svd(A)
S=np.array([[s[0],0],[0,s[1]]])

fig = plt.figure()
ax0 = fig.add_subplot(221)
ax1 = fig.add_subplot(222)
ax2 = fig.add_subplot(223)
ax3 = fig.add_subplot(224)

def plot_2D_mat(M,ax,text=""):
    ax.plot([0,M[0,0]],[0,M[1,0]],'b-o')
    ax.plot([0,M[0,1]],[0,M[1,1]],'r-o')
    ax.set_title(text)
    ax.axis('equal')
    ax.set_xlim([-1.5,1.5])
    ax.set_ylim([-1.5,1.5])
    ax.grid(True)
    

plot_2D_mat(np.eye(2),ax0,"origin")
plot_2D_mat(A,ax1,"A (USV) Matrix")
plot_2D_mat(V.T,ax2,"V Matrix")
plot_2D_mat(S.dot(V.T),ax3,"SV Matrix")

plt.show()