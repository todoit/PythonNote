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

def update_point(num):
    a = [7,6,5,4,5,6,7]
    data = bubble_sort(a, num)
    plot_bar(data)
    x = [a,a]
    

fig1 = plt.figure()

num_point = 7
a = [1,2,3,4,5,6,7]


def plot_bar(data):
    mm = 0
    for i in data:
        mm +=1
        plt.plot([mm,mm],[0,i])
        

    plt.xlabel('x')
    plt.title('bubble Sorts')
    plt.xlim(0, 8)
    plt.ylim(0, 8)
    plt.show()

# interval
# repeat
# frames
# fargs
# init_func
#anim = animation.FuncAnimation(fig1, update_point,num_point,interval=1000, repeat=True)

#anim = animation.FuncAnimation(fig1, update_point,frames=num_point, interval=50, blit=False, repeat=False)



"""
def init():
    fig_points.set_data([],[])
    return fig_points,

anim = animation.FuncAnimation(fig1, update_point,frames=num_point, init_func=init, interval=50, blit=False, repeat=False)

anim.save("anim1.mp4")
anim.save('anim1.gif', writer='imagemagick')
"""