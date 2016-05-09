#!/usr/bin/python
# -*- coding: utf-8 -*-
# CopyRight by heibanke

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

def f(t):
    s1 = np.sin(2 * np.pi * t)
    e1 = np.exp(-t)
    return np.absolute((s1 * e1)) + .05
    

def bubbleSort():
    nums = s
    for j in xrange(len(nums),-1,-1):
        for i in xrange(0,j-1,1):
            if nums[i] > nums[i+1]:
                nums[i],nums[i+1] = nums[i+1],nums[i]
                
            yield nums
    
def update(data):  
    for i in xrange(len(lines)):
        lines[i].set_ydata([0,data[i]])  
    return lines

    
t = np.arange(0.0, 5.0, 0.1)
s = f(t) 
    
fig = plt.figure(figsize=(12, 6))
ax = fig.add_subplot(111)

lines=[]

for i in xrange(len(t)):
    line,=ax.plot([i,i], [0,s[i]] , 'b-o')
    lines.append(line)

ax.set_xlabel('index')
ax.set_ylabel('value')
ax.set_title('BubbleSort')

    
ani = animation.FuncAnimation(fig, update, bubbleSort, interval=10, repeat=False)  

plt.show()