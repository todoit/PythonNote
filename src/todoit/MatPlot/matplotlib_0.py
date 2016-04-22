
# coding: utf-8
# CopyRight by heibanke

# # Matplotlib——简单图

# In[1]:

#get_ipython().magic(u'matplotlib inline')


# ## 1. 画图——基础
# 
# 了解图的基本组成部分

# In[48]:

from matplotlib import pyplot as plt

x = [1,2,3,1]
y = [1,3,0,1]

plt.plot(x,y)

#plt.title('Triangle')
#plt.ylabel('Y axis')
#plt.xlabel('X axis')

#plt.xticks([1,6])
#plt.yticks([1,6])
plt.xticks([1,6],['a','b'])

#plt.ylim([-1,4])
#plt.xlim([-1,4])

plt.grid(True,color='r')

plt.show()


# ## 2. 画图——样式

# 数据线的样式设置
# 
#     颜色缩写    全称
#     b          blue
#     c          cyan
#     g          gree
#     k          black
#     m          magenta
#     r          red
#     w          white
#     y          yellow
#    
#    
#     线型缩写    含义
#     --         --虚线
#     -.         -.虚线
#     :          .虚线
#     -          实线
#     
#     marker类型参考 
#     http://www.labri.fr/perso/nrougier/teaching/matplotlib/#line-properties

# In[11]:

from matplotlib import pyplot as plt
import numpy as np

x = [1,2,3,1]
y = [1,3,0,1]

# np.array将列表转换成numpy的数组后可以支持广播broadcast运算
plt.plot(x,y,color='r',linewidth='2',linestyle='--',marker='D', label='one')
plt.plot(np.array(x)+1,np.array(y)+1,color='g',linewidth='3',linestyle=':',marker='o', label='two')
plt.plot(np.array(x)+2,np.array(y)+3,color='k',linewidth='1',linestyle='-.',marker='>', label='three')

plt.grid(True)
plt.legend()
plt.legend(loc='upper left')

plt.show()


# ## 3. 画图——中文

# 1. 下载参考资料里的微软雅黑字体msyh.ttf
# 2. 将字体拷贝到matplotlib安装位置 /matplotlib/mpl-data/fonts/
# 3. 修改配置文件 /matplotlib/mpl-data/matplotlibrc
# 
#     1) backend      : TkAgg  #mac需要修改，windows默认就是TkAgg
#     
#     2) font.family         : Microsoft YaHei
#     
#     3) font.serif          : Microsoft YaHei, ......#(后面的不变，只在前面加雅黑字体)
#     
#     OK, 大功告成，试试效果吧

# In[6]:


from matplotlib import pyplot as plt
import numpy as np

x = [1,2,3,1]
y = [1,3,0,1]

x2 = np.array(x)+1
y2 = np.array(y)+1

plt.plot(x,y,'g',label=u'第一个', linewidth=5)
plt.plot(x2,y2,'c',label=u'第二个',linewidth=5)

plt.title(u'两个三角形')
plt.ylabel(u'Y轴')
plt.xlabel(u'X轴')

plt.legend()

plt.show()


# ## 4. 画图——公式TeX, 文本和标注支持

# In[16]:

import matplotlib.pyplot as plt
fig = plt.figure() #figsize=(10,6)
ax= fig.add_subplot(111)
ax.set_xlim([1, 6]);
ax.set_ylim([1, 9]);
ax.text(2, 8,  r"$ \mu \alpha \tau \pi \lambda \omega \tau     lambda \iota \beta $",color='r',fontsize=20);
ax.text(2, 6, r"$ \lim_{x \rightarrow 0} \frac{1}{x} $",fontsize=20);
ax.text(2, 4, r"$ a \ \leq \ b \ \leq \ c \ \Rightarrow \ a     \leq \ c$",fontsize=20);
ax.text(2, 2, r"$ \sum_{i=1}^{\infty}\ x_i^2$",fontsize=20);
ax.text(4, 8, r"$ \sin(0) = \cos(\frac{\pi}{2})$",fontsize=20);
ax.text(4, 6, r"$ \sqrt[3]{x} = \sqrt{y}$",fontsize=20);
ax.text(4, 4, r"$ \neg (a \wedge b) \Leftrightarrow \neg a     \vee \neg b$");
ax.text(4, 2, r"$ \int_a^b f(x)dx$",fontsize=20);
plt.show()


# Annotate各种格式可参考文档
# 
# http://matplotlib.org/users/annotations_guide.html#annotating-with-arrow

# In[40]:

import matplotlib.pyplot as plt

plt.figure(1, figsize=(3,3))
ax = plt.subplot(111)

ann = ax.annotate("Test",
                  xy=(0.2, 0.2), 
                  xytext=(0.8, 0.8), 
                  size=20, va="center", ha="center",
                  bbox=dict(boxstyle="round4", fc="w"),
                  arrowprops=dict(arrowstyle="-|>",
                                  connectionstyle="arc3,rad=0.2",
                                  fc="r"), 
                  )
ax.grid(True)
plt.show()


# ## 5. 画图——多子图结构

# <table class="table table-bordered">
# <tr><td>1</td><td>2</td></tr>
# 
# <tr><td>3</td><td>4</td></tr>
# </table>

# In[18]:

from matplotlib import pyplot as plt
import numpy as np

# arange类似python里的range
t = np.arange(0, 5, 0.2)

fig = plt.figure()#figsize=(10,6)

#行, 列, 序号
ax1 = fig.add_subplot(221) 
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(212)

ax1.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
ax1.grid(True)
ax1.set_title('plot')

ax2.semilogy(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
ax2.grid(True)
ax2.set_title('ylog')

ax3.loglog(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
ax3.grid(True)
ax3.set_title('loglog')

fig.suptitle('normal vs ylog vs loglog')
#fig.subplots_adjust(hspace=0.4)

plt.show()


# In[ ]:



