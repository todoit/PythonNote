# -*- coding: utf-8 -*-

'''
Created on 2016年4月21日
@author: todoit
'''

'''
三角形绕某个点旋转任意角度
'''

import matplotlib.pyplot as plt
import numpy as np

    
#对一个点进行旋转
#输入参数，a是转换前的点的坐标，p是围绕旋转的点，angle是旋转的度数
def rotatePoint(a, p, angle):
    #计算出该点到某一点的距离，即半径
    print("旋转前的点: ",a)
    #旋转后点的坐标
    b0 = p[0] + (a[0]-p[0]) * np.cos(angle * np.pi/180) - (a[1] - p[1]) * np.sin(angle * np.pi/180)
    b1 = p[1] + (a[0]-p[0]) * np.sin(angle * np.pi/180) + (a[1] - p[1]) * np.cos(angle * np.pi/180)
    b = (b0, b1)
    print("旋转后的点: ",b)
    return b

#对一个曲线图形（用两个list表示）进行旋转，返回旋转后的两个list，
#方法为对曲线中的每个点进行旋转
#输入lines是两个list,两个list的长度必须相同， angle是旋转度数
def rotateLines(lines, p, angle):
    size = len(lines[0])
    #判断两个list长度是否相等
    assert size == len(lines[1]), "两个list长度不同!"
    m,n = [None] * size, [None] * size #初始化输出结果
    for i in range(0, size):
        print(i)
        m[i],n[i] = rotatePoint((lines[0][i],lines[1][i]), p , angle)
    return m,n
    

if __name__ == '__main__':
    
    #把作业1的图画到作业2中
    
    fig = plt.figure(figsize=(10,6))#figsize=(10,6)
    #生成5个子图
    #行, 列, 序号
    ax1 = fig.add_subplot(321) 
    ax2 = fig.add_subplot(322)
    ax3 = fig.add_subplot(312)
    ax4 = fig.add_subplot(325)
    ax5 = fig.add_subplot(326)
    
    plt.xticks([-4,4])
    plt.yticks([-4,4])
    
    #三角形的初始点
    x = [1,2,3,1]
    y = [1,3,0,1]
    
    ax3.plot(x,y,'r',label=u'原始图形',linewidth=2)
    ax3.set_title("原始图形")
    
    
    p0 = (0,0)
    
    #需要旋转的度数列表45,90,270,315
    
    m,n = rotateLines([x,y], p0, 45)
    ax1.plot(m,n,'g', linewidth=3,linestyle='--')
    #===========================================================================
    # plt.sca(ax1)
    # plt.xticks([-4,4])
    # plt.yticks([-4,4])
    #===========================================================================
    ax1.grid(True)
    ax1.set_title('旋转45度')
    
    m,n = rotateLines([x,y], p0, 90)
    ax2.plot(m,n,'g', linewidth=3,linestyle='--')
    ax2.grid(True)
    ax2.set_title('旋转90度')
    
    m,n = rotateLines([x,y], p0, 270)
    ax4.plot(m,n,'g', linewidth=3,linestyle='--')
    ax4.grid(True)
    ax4.set_title('旋转270度')
    
    m,n = rotateLines([x,y], p0, 315)
    ax5.plot(m,n,'g', linewidth=3,linestyle='--')
    ax5.grid(True)
    ax5.set_title('旋转315度')
    
    fig.subplots_adjust(hspace=0.5)
    
    
    plt.show()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    