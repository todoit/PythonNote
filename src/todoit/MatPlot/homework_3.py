# -*- coding: utf-8 -*-

'''
Created on 2016年4月28日

@author: todoit
'''

'''
将冒泡排序和快速排序放到一起对比
冒泡排序的一帧表示从左到右遍历一次
快速排序的一帧表示递归深度加1（快速排序没有实现生成器的方法，每次都要从头开始，效率可能有点低）

'''


from matplotlib import pyplot as plt
import matplotlib.animation as animation
from random import randint
import os

os.chdir("E:/")

#我的电脑好像没有这个输出视频的工具，需要下载安装 
#http://stackoverflow.com/questions/13316397/matplotlib-animation-no-moviewriters-available/14574894#14574894
#设置ffmpeg路径
plt.rcParams['animation.ffmpeg_path'] = 'D:/ffmpeg/bin/ffmpeg'


'''
*****冒泡排序*****
'''

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
 

#冒泡排序生成器
def data_gen():
    return bubbleSort(data)


#冒泡排序更新函数，返回一个列表
#刚开始一直想不明白怎么一次更新多个line，在这里找到了解决方法
#http://stackoverflow.com/questions/23049762/matplotlib-multiple-animate-multiple-lines?answertab=oldest#tab-top
def update(datag):
    #循环拿到数据
    for num,line in enumerate(lines_list):
        #例如如果在x轴1的位置值y为2，画line的坐标是：x为[1,1]，y为[0,2]
        line.set_data([num,num],[0,datag[num]])
    #返回数据
    return lines_list

#冒泡排序init函数 
def init():
    for num,line in enumerate(lines_list):
        #例如如果在x轴1的位置值y为2，画line的坐标是：x为[1,1]，y为[0,2]
        line.set_data([num,num],[0,data[num]])
    #返回数据
    return lines_list



def updateAll(i):
    #快速排序
    data_bubble = next(bubble_sort_data)
    data_quick = quickSort(data, i)
    print(data_bubble)
    #循环拿到数据，更新list
    for num,line in enumerate(lines_list): 
        #如果在x轴1处值为2，line的x为[1,1]，y为[0,2]
        line.set_data([num,num],[0,data_bubble[num]])

    #循环拿到数据，更新list2
    for num,line in enumerate(lines_list2): 
        #如果在x轴1处值为2，line的x为[1,1]，y为[0,2]
        line.set_data([num,num],[0,data_quick[num]])
        
    #返回数据
    return lines_list, lines_list2 

'''
*****快速排序*****
'''
#非生成器方法，通过i来控制限制递归深度
def quickSort(data,i):
    
    #递归深度减去1
    i-=1
    #print(i)
    less = [] #放小于基准的数
    pivotList = [] #放等于基准的数
    more = [] #放大于基准的数
    #如果i<=0，则返回
    if len(data) <= 1 or i<0:
        return data
    else:
        pivot = data[0]      #将第一个值做为基准
        less = [x for x in data if x < pivot] 
        more = [x for x in data if x > pivot]
        pivotList = [x for x in data if x == pivot]
        
        #继续递归
        less = quickSort(less,i)      
        more = quickSort(more,i)
        
        return less + pivotList + more



#快速排序更新函数,使用frames来更新
def update2(i):
    data_i = quickSort(data, i)
    #print(data_i)
    #循环拿到数据
    for num,line in enumerate(lines_list2): 
        #如果在x轴1处值为2，line的x为[1,1]，y为[0,2]
        line.set_data([num,num],[0,data_i[num]])
    #返回数据
    return lines_list2 

#快速排序init函数 
def init2():
    for num,line in enumerate(lines_list2):
        #例如如果在x轴1的位置值y为2，画line的坐标是：x为[1,1]，y为[0,2]
        line.set_data([num,num],[0,data[num]])
    return lines_list2



#根据这里修改总的update函数 http://www.roboticslab.ca/wp-content/uploads/2012/11/robotics_lab_animation_example.txt

if __name__ == '__main__':

    #开始画图
    fig = plt.figure(figsize=(15,9)) 
    ax = plt.subplot(211)
    ax2 = plt.subplot(212)
    
    #生成随机整数20个
    N = 50
    large = 100 #最大值
    small = 1   #最小值
    
    data = [randint(small,large) for i in range(0,N) ]
    #数组长度
    len_data = len(data)
    
    #lines列表
    lines_list = []
    lines_list2 = []  
    for i in range(len_data):
        line, = ax.plot([], [], '-o',color='b',linewidth='1',linestyle='-',marker='o')
        line2, = ax2.plot([], [], '-o',color='b',linewidth='1',linestyle='-',marker='o')
        lines_list.append(line)
        lines_list2.append(line2)
         
    #设置坐标范围
    ax.set_xlim(-1,len_data) #x轴范围
    ax.set_ylim(0,max(data)+5) 
    ax.set_title('bubble sort')
   
    ax2.set_xlim(-1,len_data)#Y轴范围
    ax2.set_ylim(0,max(data)+5)
    ax2.set_title('quick sort')
    
    #首先构建bubblesort的生成器对象
    bubble_sort_data = bubbleSort(data)
    
    #动画
    #anim = animation.FuncAnimation(fig, update, data_gen, interval=1000, repeat=False, init_func=init)
    #anim2 = animation.FuncAnimation(fig, update2, init_func=init2, frames=len_data, interval=1000, blit=False,repeat=False)  
    # frames: number of frames to draw
    simulation = animation.FuncAnimation(fig, updateAll, blit=False, frames=100, interval=500, repeat=False)

    plt.show()

   
    
    # Set up formatting for the movie files
    #Writer = animation.writers['ffmpeg']
    #writer = Writer( metadata=dict(artist='Me'), bitrate=1800)
    #anim.save("D:/homework_3.mp4", writer=writer)
    
    
