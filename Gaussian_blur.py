#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 11:59:23 2019

@author: ayeshabhatnagar
"""

from ImageUtils import ImageUtils
import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
from matplotlib.pyplot import imread
img_utils = ImageUtils() #TODO: Implement Singleton  

deriv_ = np.array([1, -2, 1])

def derivative_2nd(deriv,axis=1,in_file="images/cameraman.tif", out_file="x_deriv_cameraman.tiff"):
    """second derivative wrt x """
    arr = img_utils.read_image(in_file)
    rows = arr.shape[0]
    cols = arr.shape[1]
    new_img = np.ones((rows,cols))
    if axis==0:
        print("HAHA")
        for m in range(rows):
            for n in range(1, cols-1):
                new_img[m, n] = deriv_[0]*arr[m,n-1] + deriv_[1]*arr[m,n] + deriv_[2]*arr[m,n+1]
        out_file = "x_deriv_cameraman.tiff"
        img_utils.write_to_file(new_img,out_file)
        return
    elif axis==1:
        print("Y derivative")
        for m in range(1,rows-1):
            for n in range(cols):
                new_img[m, n] = deriv_[0]*arr[m-1,n] + deriv_[1]*arr[m,n] + deriv_[2]*arr[m+1,n]
        out_file = "y_deriv_cameraman.tiff"
        img_utils.write_to_file(new_img,out_file)
        return
        
    

def gauss_convolve(in_file="images/cameraman.tif", out_file="result.tiff", sigma=3, kernel = 3):
    arr = img_utils.read_image(in_file)
   # arr = img_utils.preprocess_image(arr)
    gauss_ker = np.ones((kernel,kernel))
    prod = 1/(2*math.pi*pow(sigma,2))
    sigma_sqr = sigma**2
    offset = int((kernel-1)/2)


    for x in range(kernel):
            for y in range(kernel):
                new_x = x - offset
                new_y = y - offset
                gauss_ker[x,y] = prod*math.exp(-(new_x**2+new_y**2)/(2*sigma_sqr))
    
    rows = arr.shape[0]
    cols = arr.shape[1]
    new_img = np.ones((rows,cols))
    plt.imshow(gauss_ker)
    print("arr.shape %d %d, offset %d" %(rows, cols, offset))
    for m in range(offset+1, rows-offset):
        for n in range(offset+1, cols-offset):
            convolve_temp = 0
            for x in range(kernel):
                for y in range(kernel):
                    convolve_temp += gauss_ker[x,y]*arr[m+x-offset, n+y-offset]
            
            new_img[m,n] = convolve_temp
    plt.imshow(new_img)
    img_utils.write_to_file(new_img,out_file)
    
#gauss_convolve(kernel=5)
derivative_2nd(deriv_,1)  
derivative_2nd(deriv_,0)    
            