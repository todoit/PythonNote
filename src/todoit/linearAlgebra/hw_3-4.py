#!/usr/bin/env python
# coding: utf-8
#copyRight by heibanke

import numpy as np  

import time
def time_cost(f):
    def _f(*arg, **kwarg):
        start = time.clock()
        a=f(*arg,**kwarg)
        end = time.clock()
        print(f.__name__,"run cost time is ",end-start)
        return a
    return _f

   
@time_cost
def fib_opt_seq(seq):
    return [fib_opt(i) for i in seq]
    
def fib_opt(n):
    a,b,i=0,1,0
    
    while i<n:
        a,b=b,a+b
        i+=1
    else:
        return b    



#使用特征根方法求斐波那契数列
#因为只需要计算一次，写在函数外部
A = np.array([[1,1],[1,0]]);
u_0 = np.array([[1,0],]).T
#求A的特征值和特征向量 
eigVals, eigVects = np.linalg.eig(A) 

#计算S和S的逆
S = eigVects
S_inv = np.linalg.inv(S) 
#计算lambda  的值
L = np.diag(eigVals) #生成对角矩阵

def fib_eig(n):
    #计算uk，n如果过大（2000）会造成溢出，
    u_k = S.dot(L**n).dot(S_inv).dot(u_0)
    #返回第一个元素
    return u_k[0,0]

@time_cost
def fib_eig_seq(n):   
    return [fib_eig(i) for i in seq] 

        
import random
#seq = [random.randint(800,1000) for i in xrange(1000)]
seq = range(1000)
a=fib_opt_seq(seq)
#print(a)
print(a[-1])

# write Your code fib_eig_seq function
# 特征根方法计算效率明显比递归方法高，但是结果中会有小数，并非完全精确
b=fib_eig_seq(seq)
#print(b)
print(b[-1])




