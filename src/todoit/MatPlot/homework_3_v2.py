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

#mp4设置方式
#http://stackoverflow.com/questions/13316397/matplotlib-animation-no-moviewriters-available/14574894#14574894
plt.rcParams['animation.ffmpeg_path'] = 'D:/ffmpeg/bin/ffmpeg.exe'   #设置ffmpeg路径

#gif设置方式
#http://www.hankcs.com/ml/using-matplotlib-and-imagemagick-to-realize-the-algorithm-visualization-and-gif-export.html
#imageMagick下载地址：http://www.imagemagick.org/script/binary-releases.php
plt.rcParams['animation.convert_path'] = 'C:/Program Files/ImageMagick-6.9.3-Q16/convert.exe'



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


#快速排序非生成器方法，通过i来控制限制递归深度
def quickSort(data,i):
    
    #递归深度减去1
    i-=1
    #print(i)
    less = [] #放小于基准的数
    pivotList = [] #放等于基准的数
    more = [] #放大于基准的数
    #如果i<=-1，则返回，第一次i=0，i-1=-1，因为冒泡排序的第一次执行，所以这个也应该执行
    if len(data) <= 1 or i<-1:
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


#init函数 
def init():
    for num,line in enumerate(lines_list):
        line.set_data([],[])
        
    for num,line in enumerate(lines_list2):
        line.set_data([],[])
    #返回数据
    return lines_list, lines_list2

#两个图像需要共用一个更新函数
#相关例子：  http://www.roboticslab.ca/wp-content/uploads/2012/11/robotics_lab_animation_example.txt
def updateAll(i):
    #拿到数据
    data_bubble = next(bubble_sort_data)
    data_quick = quickSort(data, i)
    
    #更新list
    for num,line in enumerate(lines_list): 
        #例如在x轴1处值为2，line的x为[1,1]，y为[0,2]
        line.set_data([num+1,num+1],[0,data_bubble[num]])
    #更新list2
    for num,line in enumerate(lines_list2): 
        #如果在x轴1处值为2，line的x为[1,1]，y为[0,2]
        line.set_data([num+1,num+1],[0,data_quick[num]])
        
    #返回数据
    return lines_list, lines_list2 




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
    #画图
    for i in range(len_data):
        line, = ax.plot([], [], '-o',color='b',linewidth='1',linestyle='-',marker='o')
        line2, = ax2.plot([], [], '-o',color='b',linewidth='1',linestyle='-',marker='o')
        lines_list.append(line)
        lines_list2.append(line2)
         
    #设置坐标范围
    ax.set_xlim(0,len_data+1) #x轴范围
    ax.set_ylim(0,max(data)+1) #Y轴范围
    ax.set_title('bubble sort')
   
    ax2.set_xlim(0,len_data+1)
    ax2.set_ylim(0,max(data)+1)
    ax2.set_title('quick sort')
    
    #首先构建bubblesort的生成器
    bubble_sort_data = bubbleSort(data)
    
    #这里的frames至少应该为data的长度
    anims = animation.FuncAnimation(fig, updateAll,init_func=init, blit=False, frames=len(data), interval=500, repeat=True)
    
    plt.show()

    # FFwriter = animation.FFMpegWriter()
    # Set up formatting for the movie files fps = frames per second
    #anims.save('D:/MovWave.mp4', writer=FFwriter, fps=1,dpi=300)
    
    #anims.save('D:/homework_3.gif', fps=2, writer='imagemagick')
    
    
