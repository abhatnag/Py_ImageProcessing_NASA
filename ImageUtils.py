#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 21:53:47 2019

@author: ayeshabhatnagar
"""

import numpy as np
import os
import time
import matplotlib.pyplot as plt
from matplotlib.pyplot import imread

class ImageUtils:
    __instance = None
    """Common base class for all Image Utilities functions. Reading and writing image files, conversion to Grayscale. Displaying images """
   
   #Class private members with mangling' 
    __all__ = ['read_image','write_image','read_image','preprocess_image','write_to_file','df_columns']
    __img_file = "" #By default use this to test
    df_columns = ['max','min', 'max_diff','min_x_coord','min_y_coord']
    def __init__(self, path="images/Transposed.tiff"):  
      # if os.path.exists(path):
       #    self.__img_file = path
       """ Virtually private constructor. """
       if ImageUtils.__instance != None:
         raise Exception("This class is a singleton!")
       else:
         ImageUtils.__instance = self          
           
    @staticmethod
    def getInstance():
        """Static access method"""
        if ImageUtils.getInstance() == None:
            ImageUtils()
        return ImageUtils.__instance
    
    def read_image(self,img_file="images/Transposed.tiff"): #You can change the image file by invoking this function
        """Read value in a numpy.array. For grayscale images, the return array is MxN. For RGB images, the return value is MxNx3. 
        Format is deduced from the file. By default png is applied """
        if img_file == "":
            img_file = self.__img_file
        if os.path.exists(img_file):
            try:
                print("reading in %s" %img_file)
                img_array = imread(img_file)
                return img_array
            except IOError:
                print("The file does not exists")
                return 0 
        else:
            print("File does not exists. Terminate the flow...")
            return 0
  
    def write_image(img_arr, img_file="image_out.tif"):
       """Return value is a numpy.array. For grayscale images, the return array is MxN. For RGB images, the return value is MxNx3.
       Format is deduced from the file. By default png is applied"""
       #Get the file extension
       ext = img_file.split('.')[1]
       supported_formats = plt.gcf().canvas.get_supported_filetypes()
       if ext in supported_formats:
        try:
            plt.imsave(img_file, img_arr)
        except IOError:
          return 0 
       else:
          print("This is not a valid file format, saving it as default file name: result1.tiff")
          
    def __rgbtogray(self,img):
      """
      Y = 0.299 R + 0.587 G + 0.114 B
      Refer: https://stackoverflow.com/questions/12201577/how-can-i-convert-an-rgb-image-into-grayscale-in-python
      """
      R = np.array(img[:, :, 0])
      G = np.array(img[:, :, 1])
      B = np.array(img[:, :, 2])
    
      R = (R *.299)
      G = (G *.587)
      B = (B *.114)
      Avg = (R+G+B)
      grayImage = img
      for i in range(3):
          grayImage[:,:,i] = Avg
      plt.imshow(grayImage )
      #but we only need one plane
      return grayImage[:,:,0].reshape(grayImage.shape[0],grayImage.shape[1])
    
      
    def preprocess_image(self,img_arr):
        """A wrapper function for pre-processing image """
        print("Image successfully read with dimensions %s" %(np.shape(img_arr),))
        if(np.shape(img_arr)[-1]==3):
            print("Colored image, converting to greyscale") 
            #img_arr_gray = rgb_to_gray(img_arr)
            img_arr_grey=self.__rgbtogray(img_arr)
            plt.imshow(img_arr_grey)
            print(np.shape(img_arr_grey))
            return img_arr_grey
        else:
            print("Greyscale Image with dimensions %s " %(np.shape(img_arr),))
            plt.imshow(img_arr, cmap='gray')
            plt.imshow(img_arr)      
            return img_arr
    
    def write_to_file(self,df, filename="result.csv"):
        if filename.split(".")[1] == "tiff":
            plt.imsave(filename, df)
            return
        df.to_csv(filename, index=True, header=True)
        print("%s successfully written to" %filename)
        
        #uncomment the following for better error checking
        #get_value and set_value will soon be deprecated
        
        """  for column in df.columns:
            for idx in df[column].index:
                x = df.get_value(idx,column)
        try:
            x = x if type(x) == str else str(x).encode('utf-8','ignore').decode('utf-8','ignore')
            df.set_value(idx,column,x)
        except Exception:
            print('encoding error: {0} {1}'.format(idx,column))
            df.set_value(idx,column,'')
            pass """
        
        



#Reference: https://matplotlib.org/tutorials/introductory/images.html#sphx-glr-tutorials-introductory-images-py

# plt.imshow(arr, cmap='gray')

