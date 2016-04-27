#!/usr/bin/python
# -*- coding: utf-8 -*-
#ref  http://matplotlib.org/examples/animation/animate_decay.html
# 生成器作为参数

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def data_gen():
    t=0
    cnt = 0
    while cnt < 200:
        cnt += 1
        t += 0.2
        yield t, np.sin(2*np.pi*t) * np.exp(-t/5.)


def init():
    ax.set_ylim(-1.1, 1.1)
    ax.set_xlim(0, 10)
    line.set_data([], [])
    return line,


def update(datag):
    # update the data
    t, y = datag
    xdata.append(t)
    ydata.append(y)
    line.set_data(xdata, ydata)
    
    if max(xdata)>10:
        ax.set_xlim(max(xdata)-10, max(xdata))
    return line,
    
    
    
fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2)
ax.grid()
xdata, ydata = [], []

ani = animation.FuncAnimation(fig, update, data_gen, interval=10,
                              repeat=False, init_func=init)
plt.show()