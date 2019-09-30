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
        
'''def test_numbers_under_zero():
    tab_list=[-1, -2, -3, -4, -5, -6, -9]
    tobetested.average_above_zero(tab_list)
    with pytest.raises(ZeroDivisionError):
        1/0'''