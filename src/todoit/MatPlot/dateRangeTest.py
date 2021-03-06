# -*- coding: utf-8 -*-

'''
Created on 2016年4月25日

@author: todoit
'''
'''
http://stackoverflow.com/questions/1060279/iterating-through-a-range-of-dates-in-python
'''

from datetime import timedelta, date

def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)+1):
        yield start_date + timedelta(n)

start_date = date(2013, 12, 1)
end_date = date(2014, 3, 2)
for single_date in daterange(start_date, end_date):
    print(single_date.strftime("%Y-%m-%d"))
    
print(list(daterange(start_date, end_date)))