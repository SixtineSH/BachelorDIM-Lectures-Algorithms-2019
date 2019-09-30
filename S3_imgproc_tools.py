# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 13:48:32 2019

@author: schuhles
"""

import cv2
import numpy as np

'''img_gray=cv2.imread('python.png',0)
img_bgr=cv2.imread('python.png',1)

print("Gray levels image shape = "+str(img_gray.shape))
print("BGR image shape = "+str(img_bgr.shape))

cv2.imshow("Gray levels image", img_gray)
cv2.imshow("BGR image", img_bgr)
cv2.waitKey()'''

img=cv2.imread('rick.jpg')

cv2.imshow('input', img)
cv2.waitKey()

'''for row in range(img.shape[0]):
    for col in range(img.shape[1]):
        for cha in range(img.shape[2]):
            img[row, col, cha] = 255-img[row, col,cha]'''

img=255-img
            
cv2.imshow('inverted input', img)
cv2.waitKey()