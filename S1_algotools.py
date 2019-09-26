# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 14:17:13 2019

@author: schuhles
"""

'''If Som isn't initialized, his value might be randomize depending on the language'''

'''If all the values are below 0, the divider will b equal to 0, programms don't work well with it'''

tab_list=[1,2,3,4,5,6,-9]

import numpy as np
tab_zeros= np.zeros(12, dtype=np.int32)
tab_from_list=np.array(tab_list)

for id in range(len(tab_from_list)):
    print('tab['+str(id)+']='+str(tab_from_list[id]))
    print('tab[{index}]={val}'.format(index=id, val=tab_from_list[id]))
    
    if tab_from_list[id]>0:
        print('Youpi')

print('Finished')

def mySum(param1, param2):
    '''
    Function that sums the two input params
    Ars:
        param1: an int value
        param2: an int value
    Returns the sum
    '''
    return param1+param2

print('sumTest=', mySum(1,2))

def average_above_zero(table):
    ##
    #Function that defines the average value of the table
    som = 0
    n = 0
    for id in range(len(table)):
        if table[id] > 0 :
            som = som + table[id]
            n = n + 1
    moy = som/n
    return moy
print('Moyenne = ', average_above_zero(tab_list))