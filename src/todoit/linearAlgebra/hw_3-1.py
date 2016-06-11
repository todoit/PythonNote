#!/usr/bin/python
# -*- coding: utf-8 -*-
#copyRight by heibanke 

# Gram-Schmidt

from matplotlib import pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D


A=np.array([[1],[2],[3]])
B=np.array([[1],[1],[1]])

x=np.linspace(-0.5,1,10)

x.shape=(1,10)
xx=A.dot(x)

C=A.T.dot(B)
AA=np.linalg.inv(A.T.dot(A))

P=A.dot(AA).dot(C)
E=B-P


fig = plt.figure() 
ax = fig.gca(projection='3d')

ax.plot(xx[0,:],xx[1,:],xx[2,:],label="lineA")
ax.plot(A[0],A[1],A[2],'ko',label="A")
ax.plot([0,B[0]],[0,B[1]],[0,B[2]],'m-o',label="0B")
ax.plot([B[0][0],P[0][0]],[B[1][0],P[1][0]],[B[2][0],P[2][0]],'r-o',label="BP")
ax.plot([0,E[0]],[0,E[1]],[0,E[2]],'y-o',label="0E")

ax.legend()
ax.axis('equal')
plt.show()
