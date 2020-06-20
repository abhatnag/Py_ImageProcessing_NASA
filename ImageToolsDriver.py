#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 4 21:07:52 2019

@author: ayeshabhatnagar
This is the main Driver file
cpu timing
REference: https://stackoverflow.com/questions/15176619/timing-the-cpu-time-of-a-python-program
Response by User: https://stackoverflow.com/users/868279/shedokan
"""
from ImageUtils import ImageUtils
import pandas as pd


def max_diff(img_array, axs, filename="result.csv"):
    """computes the maximum intensity difference per row(if axis=0) or per column(if axis=1)
    And then prints to the result.csv file.
    Image manipulation using 2d Numpy arrays
    References: Argument agains tusing loops
    https://medium.com/python-pandemonium/never-write-for-loops-again-91a5a4c84baf
    https://docs.scipy.org/doc/numpy/reference/generated/numpy.apply_along_axis.html
    """
    try:
        
        df['max'] = np.amax(img_array, axis=axs)
        df['min'] = np.amin(img_array, axis=axs)
        df['max_diff'] = df['max'] - df['min']
        if(axs==0):#use tuples for coordinates
            df['min_x_coord'] = np.argmin(img_array, axis=axs)
            df['max_x_coord'] = np.argmax(img_array, axis=axs)
            df['min_y_coord'] = range(0,df.shape[0]) #take care of these redundancy/mem here
            df['max_y_coord'] = range(0,df.shape[0])
        elif(axs==1):
            df['min_y_coord'] = np.argmin(img_array, axis=axs)
            df['max_y_coord'] = np.argmax(img_array, axis=axs)
            df['min_x_coord'] = range(0,df.shape[0]) #take care of these redundancy/mem here
            df['max_x_coord'] = range(0,df.shape[0])
    except AttributeError: #AxisError will will never be raised          
            pass
            """print(df) uncomment this if you want to print to the console"""
    return df   
   
#Global variables
img_utils = ImageUtils() #TODO: Implement Singleton  
print(img_utils)

img_utils = ImageUtils.getInstance() #TODO: Implement Singleton  
print(img_utils)

#Use Transposed.tiff for testing only .. along axis= 1 : intensities 100 and 50 and 0   
def test_run(in_filename, out_filename,axs):
    try:
        arr = img_utils.read_image(in_filename)
        arr = img_utils.preprocess_image(arr)
        start = time.process_time()
        #initialize pandas dataframe 
        df = max_diff(arr, axs) #df is  changed
        end = (time.process_time() - start)*1000
        img_utils.write_to_file(df,out_filename)
        print ("Processing time for %s in %.3f milliseconds. Not factoring in the time to read/write the file" % (in_filename , end))
    except AttributeError:       
        print("Please check the function-list in ImageUtils module and try again. Here's the functions list")
        print( *dir(ImageUtils), sep = ", ")


#TODO: add multiple plots
#https://stackoverflow.com/questions/46615554/how-to-display-multiple-images-in-one-figure-correctly
df = pd.DataFrame(columns=img_utils.df_columns)     
test_run("images/cameraman.tif","result_cameraman_Rows.csv",0)

df = pd.DataFrame(columns=img_utils.df_columns)
test_run("images/baboon.png","result_baboon_Columns.csv", 1)
#Image will appear greenish because cmap='gray' has to be set




