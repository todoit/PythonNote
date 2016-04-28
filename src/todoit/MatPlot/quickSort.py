# -*- coding: utf-8 -*-

'''
Created on 2016年4月28日

@author: todoit
'''
from random import randint



def quickSort(data,i):
    
    i-=1
    print(i)
    less = []
    pivotList = []
    more = []
    if len(data) <= 1 or i<=0:
        return data
    else:
        pivot = data[0]      #将第一个值做为基准
        less = [x for x in data if x < pivot]
        more = [x for x in data if x > pivot]
        pivotList = [x for x in data if x == pivot]
        less = quickSort(less,i)      #得到第一轮分组之后，继续将分组进行下去。
        more = quickSort(more,i)
        
        return less + pivotList + more

if __name__ == '__main__':
    #生成随机数字20个
    N = 20
    data = [randint(0,100) for i in range(0,N) ]

    print(data)
    print(quickSort(data,3))
    
    