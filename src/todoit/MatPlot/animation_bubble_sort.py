#!/usr/bin/python 
# -*- coding: utf-8 -*- 
# CopyRight by heibanke

from matplotlib import pyplot as plt
import matplotlib.animation as animation
from random import randint

#快速排序
#http://stackoverflow.com/questions/36455065/error-while-choosing-a-mid-pivot-element-in-python-quick-sort
def quickSort(sequence):
    iterator = iter(sequence)
    head = next(iterator)
    try:
        tail, more = chain(next(iterator), iterator), []
        yield from quickSort(split(head, tail, more))
        yield head
        yield from quickSort(more)
    except StopIteration:
        yield head

def chain(head, iterator):
    yield head
    yield from iterator

def split(head, tail, more):
    for item in tail:
        if item < head:
            yield item
        else:
            more.append(item)


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


#init函数 
def init():
    for line in lines_list:
        line.set_data([],[])
    return lines_list


#开始画图
fig, ax = plt.subplots()

#生成随机数字20个
N = 20
data = [randint(0,100) for i in range(0,N) ]
#
len_data = len(data)

#line列表
lines_list = []
for i in range(len_data):
    line, = ax.plot([], [], '-o',color='b',linewidth='1',linestyle='-',marker='o')
    lines_list.append(line)

#设置坐标范围
ax.set_xlim(-1,len_data)
ax.set_ylim(0,max(data)+1)

anim = animation.FuncAnimation(fig, update,data_gen,interval=200, repeat=False, init_func=init)

plt.show()




"""
def init():
    fig_points.set_data([],[])
    return fig_points,

anim = animation.FuncAnimation(fig1, update_point,frames=num_point, init_func=init, interval=50, blit=False, repeat=False)

anim.save("anim1.mp4")
anim.save('anim1.gif', writer='imagemagick')
"""