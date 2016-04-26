# -*- coding: utf-8 -*-

'''
Created on 2016年4月26日
@author: todoit
'''
#BubbleSort  
def bubble_sort(param):  
    p_len = len(param)  
    for i in range(p_len):  
        for j in range(1,p_len-i):  
            if param[j-1] > param[j]:  
                #print(param[j-1],'大于', param[j])
                param[j-1],param[j]=param[j],param[j-1]  
        print(param)        
    return param  
  
def main():  
    param = [17,9,10,8,7,6,4]  
    print(bubble_sort(param))
  
if __name__=="__main__":  
    main()  