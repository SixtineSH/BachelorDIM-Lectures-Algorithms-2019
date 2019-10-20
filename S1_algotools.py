# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 14:17:13 2019

@author: schuhles
"""
'''Exercices'''

'''If Som isn't initialized, his value might be randomized depending on the language'''

'''If all the values are below 0, the divider will be equal to 0, programms don't work well with it'''



tab_list=[1,2,3,4,5,6,-9]


'''AVERAGE ABOVE ZERO'''
def average_above_zero(table):
    ##
    #Function that defines and return the average of the positive values of the list
    #Args : a list of values
    #Returns : the average of positives values
    #Raises ValueError if input param is not a list, if the list is empty and if the list doesn't contain any positive value
    if not(isinstance(table, list)):
        raise ValueError('average_above_zero, expected a list as input')
    if len(table)==0:
        raise ValueError('average_above_zero, expected a non empty list as input')
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

#test section
#test, lastID=average_above_zero(tab_list)
#Kprint('test_sum=', test)



'''
MAX VALUE 

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
    #Raises ValueError if the input is not a list, if the list is empty and if the list doesn't contain numbers
    if not(isinstance(table, list)):
        raise ValueError('function_max_value, expected a list as input')
    if len(table)==0:
        raise ValueError('function_max_value, expected a non empty list as input')
    if not(isinstance(table[0], (int, float))):
        raise ValueError('function_max_value, expected a list of numbers')
    max_value = 0
    max_index = 0
    for id in range(len(table)):
        if table[id] > max_value :
            max_value = table[id]
            max_index = id
    return (max_value, max_index)
    print('maximum = ', max_value)

'''
REVERSE TABLE

size <- NMAX
index <- size - 1
iterations <- size / 2
for i <- 1 to NMAX do
    Temp <- Tab[index]
    Tab[index] <- Tab[i]
    Tab[i] <- Temp
    Index <- Index - 1
Display(Tab)
'''

def function_reverse_table(table):
    ##
    #Function that reverses the array
    #Args : a table
    #Returns : the reversed table
    #Raises ValueError if the input is not a list and if the list is empty
    if not(isinstance(table, list)):
        raise ValueError('function_reverse-table, expected a list as input')
    if len(table)==0:
        raise ValueError('function_reverse_table, expected a non empty list as input')
    size = len(table)
    index = size - 1
    its = size // 2
    for i in range(its):
        temp = table[index]
        table[index] = table[i]
        table[i] = temp
        index -= 1
    return (table)
    
'''
BOUNDING BOX

Bounding box
for i <- 1 to NMAX do
    for i <- 
        for j <- 
        
'''