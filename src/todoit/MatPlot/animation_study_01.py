#!/usr/bin/python 
# -*- coding: utf-8 -*- 
# CopyRight by heibanke

from matplotlib import pyplot as plt
import matplotlib.animation as animation
import numpy as np


def update_point(num):
    fig_points.set_data(data[:, 0:num])
    return fig_points,

fig1 = plt.figure()

num_point = 50
data = np.random.rand(2, num_point)
fig_points, = plt.plot([], [], 'ro')

plt.xlim(0, 1)
plt.ylim(0, 1)
plt.xlabel('x')
plt.title('Scatter Point')

# interval
# repeat
# frames
# fargs
# init_func
anim = animation.FuncAnimation(fig1, update_point,num_point)

#anim = animation.FuncAnimation(fig1, update_point,frames=num_point, interval=50, blit=False, repeat=False)

plt.show()

"""
def init():
    fig_points.set_data([],[])
    return fig_points,

anim = animation.FuncAnimation(fig1, update_point,frames=num_point, init_func=init, interval=50, blit=False, repeat=False)

anim.save("anim1.mp4")
anim.save('anim1.gif', writer='imagemagick')
"""