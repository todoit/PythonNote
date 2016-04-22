#!/usr/bin/python
# -*- coding: utf-8 -*-
#copyRight by heibanke 

import matplotlib.pyplot as plt

from todoit.MatPlot.homework1_circle import gen_circle_point

N=16

fig = plt.figure()

for p1,p2 in gen_circle_point(N-1):
    plt.plot(p1[0],p1[1],'b.')
    plt.plot(p2[0],p2[1],'r')

plt.show()

