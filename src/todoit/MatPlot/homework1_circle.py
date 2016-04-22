# -*- coding: utf-8 -*-

'''
Created on 2016年4月22日
@author: todoit
'''
'''
 思路： 两个共用一条边的正三角形都围绕其中一个三角形的中心旋转
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
    
def gen_circle_point(num):
    
    #从上面三角形旋转得到的灵感，定义了两个正三角形，共用一条边。
    #两个三角形都围绕其中一个三角形的中心旋转
    #最后去掉外部三角形的底边，去掉内部三角形中除公用边外的两个边
   
    #内部正三角形
    x = [-1,1]
    y = [0,0]
    
    #内部三角形的中心为，需要围绕该点旋转
    p = (0, np.tan(30*np.pi/180))
    
    #外部正三角形
    x1 = [-1,0,1]
    y1 = [0,-3**0.5,0]
    
    plt.xticks([-3,-2,-1,0,1,2,3])
    plt.yticks([-3,-2,-1,0,1,2,3])
    
    plt.ylim([-3,3])
    plt.xlim([-3,3])
    
    #plt.plot(x1,y1)

    #把圆分成num+1等分，,每个角度的度数为360%(num+1)，围绕点p进行旋转
    
    #返回的内外部点的list
    result_list = []
    angle = 0
    while angle <= 120:
        result_list.append([rotateLines([x,y], p, angle),rotateLines([x1,y1], p, angle)])
        result_list.append([rotateLines([x,y], p, angle+120),rotateLines([x1,y1], p, angle+120)])#加上120度可以和相对应的三角形连起来,成为直线
        result_list.append([rotateLines([x,y], p, angle+240),rotateLines([x1,y1], p, angle+240)])#加上240度可以和相对应的三角形连起来,成为直线
        angle += 360/(num+1)   
        
    return result_list
    



if __name__ == '__main__':
    N=12
    fig = plt.figure()

    for p1,p2 in gen_circle_point(N-1):
        plt.plot(p1[0],p1[1],'b.')
        plt.plot(p2[0],p2[1],'r')

    plt.show()
    
    
    
    