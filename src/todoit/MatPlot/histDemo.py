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


#http://matplotlib.org/api/pyplot_api.html

'''
bins 参数

bins : integer or array_like, optional

If an integer is given, bins + 1 bin edges are returned, consistently with numpy.histogram() for numpy version >= 1.3.

Unequally spaced bins are supported if bins is a sequence.

default is 10 如果不指定，默认10
'''



'''
上次错误原因，有的月份中有些日期没有。比如9月份中9月4号没有，导致天数少了一天，但是hist在画图的时候，把日期当成了连续的数据类型，他并不知道哪天没有，所以可能会将其中的有些数据合并
因此不能用这种方式
必须用range的方式，但是试用了一下range方法，里面不能传入date类型
在网上搜了一下，这里有个解决方法 
http://stackoverflow.com/questions/1060279/iterating-through-a-range-of-dates-in-python
http://stackoverflow.com/questions/7274267/print-all-day-dates-between-two-dates


'''


'''
返回值
n : array or list of arrays

The values of the histogram bins. See normed and weights for a description of the possible semantics. If input x is an array, then this is an array of length nbins. If input is a sequence arrays [data1, data2,..], then this is a list of arrays with the values of the histograms for each of the arrays in the same order.

bins : array

The edges of the bins. Length nbins + 1 (nbins left edges and right edge of last bin). Always a single array even when multiple data sets are passed in.

patches : list or list of lists

Silent list of individual patches used to create the histogram or list of such list if multiple input datasets.

sorted(2015-12,2015-11,2015-11 ,2015-09,2015-10,2015-08,2015-07  )
   209
    205
    128
    107


'''

x = list(range(1,11))
print(x)

fig, (ax0, ax1) = plt.subplots(ncols=2, figsize=(8, 4))

n,bins,patch = ax0.hist(x, bins=len(x), normed=0, histtype='bar', facecolor='g',  alpha=0.75)
ax0.set_title('stepfilled')
print('n:',n)
print('bins: ',bins)
print('patch:', patch)


# Create a histogram by providing the bin edges (unequally spaced).
bins = x
ax1.hist(x, bins=range(1,11), normed=0, histtype='bar')
ax1.set_title('unequal bins')

plt.tight_layout()
plt.show()