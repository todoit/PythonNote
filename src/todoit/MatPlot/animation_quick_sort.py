#!/usr/bin/python 
# -*- coding: utf-8 -*- 
# CopyRight by heibanke

from matplotlib import pyplot as plt
import matplotlib.animation as animation
from random import randint

#快速排序
#http://stackoverflow.com/questions/36455065/error-while-choosing-a-mid-pivot-element-in-python-quick-sort
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

#更新函数，返回一个列表
#刚开始一直想不明白怎么一次更新多个line，在这里找到了解决方法
#http://stackoverflow.com/questions/23049762/matplotlib-multiple-animate-multiple-lines
def update(i):
    print("第",i,"次")
    data_i = quickSort(data, i)
    print(data_i)
    #循环拿到数据
    for num,line in enumerate(lines_list): 
        #如果在x轴1处值为2，line的x为[1,1]，y为[0,2]
        line.set_data([num,num],[0,data_i[num]])
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


anim = animation.FuncAnimation(fig, update, init_func=init, frames=10, interval=2000, blit=False,repeat=False)  
plt.show()




"""
def init():
    fig_points.set_data([],[])
    return fig_points,

anim = animation.FuncAnimation(fig1, update_point,frames=num_point, init_func=init, interval=50, blit=False, repeat=False)

anim.save("anim1.mp4")
anim.save('anim1.gif', writer='imagemagick')
"""