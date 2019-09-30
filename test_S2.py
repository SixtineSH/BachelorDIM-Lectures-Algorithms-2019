# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 09:11:05 2019

@author: schuhles
"""

import S1_algotools_mien as tobetested
import pytest

def test_average_above_zero_working1():
    tab_list=[1,2,3,-5,6,-9]
    test=tobetested.average_above_zero(tab_list)
    assert test==3

def test_average_above_zero_empty_table():
    tab_list=[]
    with pytest.raises(ValueError):
        tobetested.average_above_zero(tab_list)

def test_average_above_zero_dividedbyzero():
    tab_list=[-1, -2, -3, -5, -6, -9]
    with pytest.raises(ValueError):
        tobetested.average_above_zero(tab_list)
        
def test_average_above_zero_no_list():
    tab_list=12
    with pytest.raises(ValueError):
        tobetested.average_above_zero(tab_list)
        
def test_average_above_zero_non_numbers():
    tab_list=['a', 'ef', 'dzv', 'cdz', 'dc']
    with pytest.raises(ValueError):
        tobetested.average_above_zero(tab_list)


def test_function_max_value_working1():
    tab_list=[1,2,3,-5,6,-9]
    test=tobetested.function_max_value(tab_list)
    assert test==(6,4)

def test_function_max_value_empty_table():
    tab_list=[]
    with pytest.raises(ValueError):
        tobetested.function_max_value(tab_list)
        
def test_function_max_value_no_list():
    tab_list=250
    with pytest.raises(ValueError):
        tobetested.function_max_value(tab_list)
        
def test_function_max_value_non_numbers():
    tab_list=['12', '15', '125', '512', '2048']
    with pytest.raises(ValueError):
        tobetested.function_max_value(tab_list)