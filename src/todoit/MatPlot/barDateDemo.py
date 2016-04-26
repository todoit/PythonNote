# -*- coding: utf-8 -*-

'''
Created on 2016年4月25日

@author: todoit
'''
"""
Demo of the histogram (hist) function with different ``histtype`` settings.

* Histogram with step curve that has a color fill.
* Histogram with with unequal bin widths.

"""
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, date
import matplotlib.dates as mdates


'''
日期格式如何在bar中画图
如果传入的x中日期格式不连续，则在bar画图中自动回将其连续排列，而且会自动将中间没有的时间加上去
'''
#http://matplotlib.org/api/pyplot_api.html

date1 = date(2016, 2, 26)
date2 = date(2016, 3, 1)
date3 = date(2016, 3, 2)
print(date1, date2,date3)
x = [date1, date2, date3]
y = [1,2,3]

#设置日期的格式
myFmt = mdates.DateFormatter('%Y-%m-%d')

fig, (ax0, ax1) = plt.subplots(ncols=2, figsize=(8, 4))

ax0.bar(x,y, facecolor='g',  alpha=0.75, align='center')
#将日期格式设置到图中
ax0.xaxis.set_major_formatter(myFmt)

# Create a histogram by providing the bin edges (unequally spaced).

plt.tight_layout()
plt.show()