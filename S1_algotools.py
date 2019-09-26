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

'''Exercices'''

def average_above_zero(table):
    ##
    #Function that defines and return the average value of the list
    #Args : a list of values
    #Returns : the average of positives values
    #Raises ValueError if input param is not a list
    if not(isinstance(table, list)):
        raise ValueError('average_above_zero, expected a list as input')
    if len(table)==0:
        raise ValueError('expected a non empty list as input')
    if not(isinstance(table[0], (int, float))):
        raise ValueError('average_above_zero, expected a list of numbers')
    som = 0
    n = 0
    for id in range(len(table)):
        if table[id] > 0 :
            som = som + table[id]
            n = n + 1
    if n == 0:
        raise ValueError('Division by 0')    
    return som / n
print('Moyenne = ', average_above_zero(tab_list))

'''
max <- 0
for i <- 1 to NMAX do
    if Tab[i] > Max then
        Max <- Tab[i]
        IndexMax <- i
Display(Max, i)
'''

def function_max_value(table):
    ##
    #Function that finds and return the maximum value of the list
    #Args : a list of values
    #Returns : the maximum value of the list
    #Raises ValueError
    if not(isinstance(table, list)):
        raise ValueError('function_max_value, expected a list as input')
    if len(table)==0:
        raise ValueError('expected a non empty list as input')
    if not(isinstance(table[0], (int, float))):
        raise ValueError('function_max_value, expected a list of numbers')
    max_value = 0
    max_index = 0
    for id in range(len(table)):
        if table[id] > max_value :
            max_value = table[id]
            max_index = id
    return (max_value, max_index)
print('Valeur max = ', function_max_value(tab_list))
                