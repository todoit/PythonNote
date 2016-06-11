#!/usr/bin/env python
# coding: utf-8
#copyRight by heibanke

import numpy as np
import matplotlib.pyplot as plt  

#pca主成分分析
def pca(dataMat, topNfeat=5):  
    #print(dataMat)
    meanVals = np.mean(dataMat, axis=0)  
    print(meanVals)
    meanRemoved = dataMat - meanVals                #减去均值  
    covMat = meanRemoved.T.dot(meanRemoved)         #求协方差方阵  
    eigVals, eigVects = np.linalg.eig(covMat)       #求特征值和特征向量  
    eigValInd = np.argsort(eigVals)                 #对特征值进行排序  
    eigValInd = eigValInd[:-(topNfeat + 1):-1]    
    redEigVects = eigVects[:, eigValInd]            #除去不需要的特征向量  
    lowDDataMat = meanRemoved.dot(redEigVects)      #求新的数据矩阵  
    reconMat = (lowDDataMat.dot(redEigVects.T)) + meanVals  
    reduceData = lowDDataMat + np.mean(dataMat)

    return reduceData,reconMat  
    
N=100
x=np.linspace(2,4,N)
y=x*2-4

x1=x+(np.random.rand(N)-0.5)*1.5
y1=y+(np.random.rand(N)-0.5)*1.5

data = np.array([x1,y1])
a,b=pca(data.T,1)

plt.plot(x,y,color='g',linestyle='-',marker='',label='ideal') 
plt.plot(x1,y1,color='b',linestyle='',marker='o',label='noise')
plt.plot(b[:,0],b[:,1],color='r',linestyle='',marker='>',label='recon')
plt.plot(a[:,0],np.zeros(N),color='k',linestyle='',marker='*',label='lowD')

plt.legend()
plt.axis('equal')

plt.show()