#!/usr/bin/python 
# -*- coding: utf-8 -*- 
# CopyRight by heibanke

from matplotlib import pyplot as plt
import matplotlib.animation as animation
from random import randint




#快速排序
#快速排序研究了很长时间，但是仍然没有实现生成器的方法。
#目前的方法是在上面指定递归的深度，每次都要重新开始递归，从效率上来说肯定要比生成器方法低
def quickSort(data,i):
    
    i-=1
    print(i)
    print('这次排序的数据是:', data)
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



#冒泡排序
def bubbleSort(data):
   #冒泡排序
    size = len(data)
    for i in range(size):  
        for j in range(1,size-i):  
            if data[j-1] > data[j]:  
                data[j-1],data[j]=data[j],data[j-1] 
            print(data)
            #每一次比较都返回数据
            #如果把yield前移，就是老师的fast方法
        yield data  
 

#生成器
def data_gen():
    return bubbleSort(data)

#更新函数，返回一个列表
#刚开始一直想不明白怎么一次更新多个line，在这里找到了解决方法
#http://stackoverflow.com/questions/23049762/matplotlib-multiple-animate-multiple-lines
def update(datag):
    #循环拿到数据
    for num,line in enumerate(lines_list):
        #如果在x轴1处值为2，line的x为[1,1]，y为[0,2]
        line.set_data([num,num],[0,datag[num]])
    #返回数据
    return lines_list

def update2(i):
    data_i = quickSort(data, i)
    print(data_i)
    #循环拿到数据
    for num,line in enumerate(lines_list2): 
        #如果在x轴1处值为2，line的x为[1,1]，y为[0,2]
        line.set_data([num,num],[0,data_i[num]])
    #返回数据
    return lines_list2 



#init函数 
def init():
    for line in lines_list:
        line.set_data([],[])
    return lines_list

#init函数 
def init2():
    for line in lines_list2:
        line.set_data([],[])
    return lines_list2


#开始画图
fig = plt.figure(1) 
ax = plt.subplot(211)
ax2 = plt.subplot(212)

#生成随机数字20个
N = 50
data = [randint(0,100) for i in range(0,N) ]
#
len_data = len(data)

#line列表
lines_list = []
for i in range(len_data):
    line, = ax.plot([], [], '-o',color='b',linewidth='1',linestyle='-',marker='o')
    lines_list.append(line)

lines_list2 = []  
for i in range(len_data):
    line2, = ax2.plot([], [], '-o',color='b',linewidth='1',linestyle='-',marker='o')
    lines_list2.append(line2)

#设置坐标范围
ax.set_xlim(-1,len_data)
ax.set_ylim(0,max(data)+1)

anim = animation.FuncAnimation(fig, update,data_gen,interval=1000, repeat=False, init_func=init)
anim2 = animation.FuncAnimation(fig, update2, init_func=init2, frames=len_data, interval=1000, blit=False,repeat=False)  

ax2.set_xlim(-1,len_data)
ax2.set_ylim(0,max(data)+1)

plt.show()




"""
def init():
    fig_points.set_data([],[])
    return fig_points,

anim = animation.FuncAnimation(fig1, update_point,frames=num_point, init_func=init, interval=50, blit=False, repeat=False)

anim.save("anim1.mp4")
anim.save('anim1.gif', writer='imagemagick')
"""