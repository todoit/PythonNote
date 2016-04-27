#!/usr/bin/python 
# -*- coding: utf-8 -*- 
# CopyRight by heibanke

from matplotlib import pyplot as plt
import matplotlib.animation as animation
import numpy as np


#BubbleSort  
#两个参数，返回第n次循环时的数组状态
def bubble_sort(data, num):  
    p_len = len(data)
    n = 0
    for i in range(len(data)):  
        for j in range(1,p_len):  
            n += 1
            if n > num: 
                break
            else:
                if data[j-1] > data[j]:  
                    data[j-1],data[j]=data[j],data[j-1]  
    return data  

#生成器
def data_gen():
    data = [8,6,4]
    size = len(data)
    num = 0;
    for i in range(size):  
        for j in range(1,size-i):  
            num += 1
            if data[j-1] > data[j]:  
                data[j-1],data[j]=data[j],data[j-1] 
            print(data)
            yield data 

 
def update(datag):
    # update the data
    size = len(datag)
    #返回数据
    mm = 0
    for data in datag:
        mm+=1
        line[i].set_data([mm,mm],[0,data])
    return lines_list,    


 

fig, ax = plt.subplots()

lines_list = []
for i in range(3):
    line, = ax.plot([0],[i])
    lines_list.append(line)

xdata1, ydata1, xdata2,ydata2, xdata3, ydata3 = [], [],[],[],[],[]

#anim = animation.FuncAnimation(fig, update,data_gen,interval=1000, repeat=False, init_func=init)

plt.show()



# interval
# repeat
# frames
# fargs
# init_func


#anim = animation.FuncAnimation(fig, update_point,frames=num_point, interval=50, blit=False, repeat=False)



"""
def init():
    fig_points.set_data([],[])
    return fig_points,

anim = animation.FuncAnimation(fig1, update_point,frames=num_point, init_func=init, interval=50, blit=False, repeat=False)

anim.save("anim1.mp4")
anim.save('anim1.gif', writer='imagemagick')
"""