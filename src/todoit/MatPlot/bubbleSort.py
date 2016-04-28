# -*- coding: utf-8 -*-

'''
Created on 2016年4月26日
@author: todoit
'''
#BubbleSort  
#冒泡排序，生成器方法
def bubbleSort(data):
    size = len(data)
    for i in range(size):  
        for j in range(1,size-i):  
            if data[j-1] > data[j]:  
                data[j-1],data[j]=data[j],data[j-1] 
            #print(data)
            #每一次比较都返回数据
            #如果把yield放到第二个循环中，就是老师的slow方法，目前是老师的fast方法
        yield data  
 

    
  
if __name__=="__main__":  
    param = [17,9,10,8,7,6,4]  
    data = bubbleSort(param)
    i = 10
    while i>=0:
        print(next(data))
        i-=1
    
    
    
    