#!/usr/bin/env python
# coding: utf-8
#copyRight by heibanke

import numpy as np
import matplotlib.pyplot as plt  
from load_MNIST import *
from solutions_3 import *


trainX,trainy,testX,testy=get_data(Only0=False,N=2000)
data=trainX[:,1:]

"""
# write Your code
# def pca(data,k=0.9):
    # data 原始的图片
    # k是保留特征值的百分比
    # return 返回降维后重建的图片

# def show_pic(origin_data, low_dim_):

# N is number of pic to show in the figure
"""
N = 20
recon_data = pca(data,k=0.9)
show_pic(data[:N,:],recon_data[:N,:])

