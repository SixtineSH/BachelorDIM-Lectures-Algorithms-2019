# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 09:11:05 2019

@author: schuhles
"""

import S1_algotools_mien as tobetested
import pytest


def test_average_above_zero_working1():
    tab_list=[1,2,3,4,-5,6,-9]
    test, lasID=tobetested.average_above_zero(tab_list)
    assert test==3

def test_average_above_zero_table():
    tab_list=[1,2,3,4,-5,6,-9]

def test_average_above_zero_dividebyzero():
    with pytest.raises(ZeroDivisionError):
        1/0