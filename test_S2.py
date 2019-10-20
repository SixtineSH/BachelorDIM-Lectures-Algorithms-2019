# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 09:11:05 2019

@author: schuhles
"""

import S1_algotools as tobetested
import pytest

'''Test Average Above Zero'''

def test_averageAboveZero_working1():
    tab_list=[1,2,3,-5,6,-9]
    test=tobetested.average_above_zero(tab_list)
    assert test==3

def test_averageAboveZero_empty_table():
    tab_list=[]
    with pytest.raises(ValueError):
        tobetested.average_above_zero(tab_list)

def test_averageAboveZero_dividedbyzero():
    tab_list=[-1, -2, -3, -5, -6, -9]
    with pytest.raises(ValueError):
        tobetested.average_above_zero(tab_list)
        
def test_averageAboveZero_no_list():
    tab_list=12
    with pytest.raises(ValueError):
        tobetested.average_above_zero(tab_list)
        
def test_averageAboveZero_non_numbers():
    tab_list=['a', 'ef', 'dzv', 'cdz', 'dc']
    with pytest.raises(ValueError):
        tobetested.average_above_zero(tab_list)

'''Test Max Value'''

def test_functionMaxValue_working1():
    tab_list=[1,2,3,-5,6,-9]
    test=tobetested.function_max_value(tab_list)
    assert test==(6,4)

def test_functionMaxValue_empty_table():
    tab_list=[]
    with pytest.raises(ValueError):
        tobetested.function_max_value(tab_list)
        
def test_functionMaxValue_no_list():
    tab_list=250
    with pytest.raises(ValueError):
        tobetested.function_max_value(tab_list)
        
def test_functionMaxValue_non_numbers():
    tab_list=['12', '15', '125', '512', '2048']
    with pytest.raises(ValueError):
        tobetested.function_max_value(tab_list)
        
'''Test Reverse Table'''
        
def test_functionReverseTable_empty_table():
    tab_list=[]
    with pytest.raises(ValueError):
        tobetested.function_reverse_table(tab_list)
        
def test_functionReverseTable_no_list():
    tab_list=75
    with pytest.raises(ValueError):
        tobetested.function_reverse_table(tab_list)
        
'''Test Bounding Box'''
        
def test_functionRoiBBox_no_np():
    with pytest.raises(ValueError):
        tobetested.function_roi_bbox(9)

def test_functionRoiBbox_empty_array():
    with pytest.raises(ValueError):
        tobetested.function_roi_bbox([])