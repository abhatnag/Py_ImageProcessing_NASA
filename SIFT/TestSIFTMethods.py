#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  3 19:01:04 2019

@author: ayeshabhatnagar
"""

import cv2 
import unittest
import numpy as np


""" n-w+1 n-h+1 multiplications with the window"""
class TestSIFTMethods(unittest.TestCase):
    test_img1 = None
    def setUp(self):
        ls = []
        for i in range(5):
            ls.append([*range(0,5)])
        self.test_img1 = np.array(ls,dtype=np.uint8)
        print("Are we there yet")
        cv2.imshow('hello',self.test_img1)
        cv2.destroyWindow('hello')
           
    def __init__(self):
       # self.img = cv2.createMatrix(5,5,CV_8UC1)
        self.img = [[range(5)], [range(5)]]
        print(self.img)
    def test_upper(self):
        self.assertTrue('FOO'.isupper())
        


tt = TestSIFTMethods()
tt.test_upper()

