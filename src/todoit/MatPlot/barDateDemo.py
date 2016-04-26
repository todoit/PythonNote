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
import matplotlib.pyplot as plt
from datetime import  date
import matplotlib.dates as mdates
import matplotlib
#设置美化格式
plt.style.use('ggplot')  

matplotlib.rcParams.update({'font.size': 15})

'''
日期格式如何在bar中画图

如果传入的x中日期格式不连续，则在bar画图中自动补全缺失数据
而且会自动按升序排列
'''
#http://matplotlib.org/api/pyplot_api.html

date1 = date(2016, 2, 26)
date2 = date(2016, 3, 2)
date3 = date(2016, 3, 1)
date4 = date(2016, 3, 5)

#日期不连续
x = [date1, date2, date3, date4]
y = [1,2,3,4]

#设置日期的格式
myFmt = mdates.DateFormatter('%Y-%m-%d')

fig, ax0 = plt.subplots(ncols=1, figsize=(8, 4))
#画柱状图
ax0.bar(x,y, align='center')
#将日期格式设置到图中
ax0.xaxis.set_major_formatter(myFmt)
plt.show()