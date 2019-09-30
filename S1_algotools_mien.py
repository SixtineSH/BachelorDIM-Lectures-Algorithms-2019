# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 14:17:13 2019

@author: schuhles
"""

'''If Som isn't initialized, his value might be randomize depending on the language'''

'''If all the values are below 0, the divider will b equal to 0, programms don't work well with it'''

tab_list=[1,2,3,-5,6,-9]

import numpy as np
tab_zeros= np.zeros(12, dtype=np.int32)
tab_from_list=np.array(tab_list)

'''for id in range(len(tab_from_list)):
    print('tab['+str(id)+']='+str(tab_from_list[id]))
    print('tab[{index}]={val}'.format(index=id, val=tab_from_list[id]))
    
    if tab_from_list[id]>0:
        print('Youpi')

print('Finished')'''

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

'''#test section
tab_list=[1,2,3,4,5,6,-9]
test, lasID=average_above_zero(tab_list)
print('test_sum=', test)'''

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
    size = len(table)
    index = size - 1
    its = size // 2
    for i in range(its):
        temp = table[index]
        table[index] = table[i]
        table[i] = temp
        index -= 1
print ('Liste ', tab_list)
function_reverse_table(tab_list)
print ('Liste inversée ',tab_list)
    
'''
Bounding box
for i <- 1 to NMAX do
    for i <- 
        for j <- 
        
'''

'''import numpy as np
matrix = np.zeros((10,10), dtype=np.int32)

matrix[3:6, 4:8]=np.ones((3,4), dtype=np.int32)

import cv2
img=cv2.imread('Image.png', 0)
cv2.imshow('read image', img)
cv2.waitKey()

for idrow in range(matrix.shape[0]):
    for idcol in range(matrix.shape[1]):
        pixVal=matrix[idrow, idcol]'''
        
#x,y,w,h = cv2.boundingRect(cnt) for x,y top-left coordinates and w,h bottom-right coordinates
#img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
            
'''top = H
bottom = 0
left = 
right = 
for col in range (L):
    for row in range (H):
        if mat[row,col] == 1:
            if top > row:
                top = row
            if bottom < row:
                bottom = row
            if left < col:
                left = col
            if right > col:
                right = col
        if top == -1: #4 boucles en parallèle
            top = row
            break
        if top != -1:
            break'''
        
            