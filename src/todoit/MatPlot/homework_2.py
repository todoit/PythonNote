# -*- coding: utf-8 -*-

'''
Created on 2016年4月24日
@author: todoit
'''
import csv
from datetime import datetime
import os
from matplotlib import pyplot as plt
import numpy as np
    
#设置美化格式
plt.style.use('ggplot')


os.chdir("E:\\workspace_python\\PythonNote\\src\\todoit\\MatPlot") # 改变目录，注意双引号和反斜杠
#星期字典
week_dict = {1:'星期一', 2:'星期二', 3:'星期三', 4:'星期四', 5:'星期五', 6:'星期六', 7:'星期日'}

#将文件读到dict的list中
def readOrders(file_name): 
    orders_data = [] 
    #时间格式
    time_str = '%m/%d/%Y %H:%M'
    
    with open(file_name,'r') as f:
        f_reader = csv.reader(f)
        #跳过第一行
        headings = next(f_reader)
        for row in f_reader:
            order={}
            order['id'] = row[0]
            order['money'] = float(row[1])
            order['channel'] = row[2]
            #从字符串得到日期类型
            date = datetime.strptime(row[3], time_str)
            order['datetime']=date
            #星期
            order['week'] = week_dict[date.weekday()+1]
            #年和月组成的字符串
            order['year_monty'] = str(date.year)+'-'+str(date.month)
            
            orders_data.append(order)
    print(orders_data)
    #返回结果按照时间排序
    return sorted(orders_data,key=lambda order: order['id'])


#用户分析
def userAnalysis(orders_data):

    fig = plt.figure(figsize=(9,20))#figsize=(10,6)

    #行, 列, 序号
    ax0 = fig.add_subplot(311) 
    ax1 = fig.add_subplot(323)
    ax2 = fig.add_subplot(324)
    ax3 = fig.add_subplot(313)
    
    #用户增长趋势分析，按天
    N = 1 #设置分布宽度
    orders_date_list = [order['datetime'].date() for order in orders_data]
    ax0.hist(orders_date_list, len(set(orders_date_list))/N-0.5, normed=0, histtype='bar', facecolor='g', alpha=1)
    ax0.set_title('用户数量增长情况-按天')
    
    
    
    ##用户增长趋势分析，按月分析
    month_list = [order['datetime'].month for order in orders_data]
    #每月的新增用户数
   
    
    ax1.hist(month_list, len(set(month_list))-0.5,  normed=0, histtype='bar', facecolor='g', alpha=0.75)
    ax1.set_xlabel("时间")
    ax1.set_title('用户数量增长情况-按月')
    
       
    #分析用户购买时间，按照星期分析
    orders_week_list = [order['datetime'].weekday()+1  for order in orders_data]
    ax2.hist(orders_week_list, len(set(orders_week_list)), normed=0, histtype='bar', facecolor='g', alpha=0.75)
    ax2.set_xticklabels([week_dict[i] for i in range(1,8)])
    ax2.set_title('用户数量增长情况-按周')
    
    
    #按照每天的时段进行分析
    orders_hour_list = [order['datetime'].hour for order in orders_data]
    ax3.hist(orders_hour_list, len(set(orders_hour_list)), normed=0, histtype='bar', facecolor='g', alpha=0.75)
    ax3.set_title('用户数量增长情况-每天不同时间段分析')
    
    fig.subplots_adjust(hspace=0.7)
    plt.show()

# 支付分析
def courseAnalysis(orders_data):
    from matplotlib import pyplot as plt
    import numpy as np
    import matplotlib.cm as cm
    import itertools
    
    fig,(ax0,ax1)=plt.subplots(nrows=2, figsize=(9,6))
    
    #分析价格随时间变化趋势
    #价格变化趋势分析，对每种支付方式分别分析，看是否针对不同的支付方式有不同的价格
    #得到支付方式列表
    channels = set(order['channel'] for order in orders_data)
    colors =   iter(cm.rainbow(np.linspace(0, 1, len(channels))))
    for channel in channels:
        date_list = [order['datetime'] for order in orders_data if order['channel']==channel]
        price_list = [order['money'] for order in orders_data if order['channel']==channel]
        ax0.scatter(date_list,price_list,label=channel,s=5,color=next(colors))
        ax0.legend()
    
    
    #每天的收入分析
    #时间列表
    date_list = set(order['datetime'].month for order in orders_data)
    #每天的总收入
    date_money_dict = {}
    for date in date_list:
        date_money_dict[date] = sum(order['money'] for order in orders_data if order['datetime'].month == date) 
    ax1.bar(range(len(date_money_dict)), date_money_dict.values(), align='center')
    #ax1.xticks(range(len(date_money_dict)), date_money_dict.keys())
    
    plt.show()
    
    
    
    

if __name__ == '__main__':
    orders_data = readOrders("OutOrder.csv")
    
    userAnalysis(orders_data)
    courseAnalysis(orders_data)
    
    
    
    
    
    




