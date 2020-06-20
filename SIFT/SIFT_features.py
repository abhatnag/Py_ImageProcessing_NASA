#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  3 18:37:51 2019

@author: ayeshabhatnagar
"""

from ImageUtils import ImageUtils
import pandas as pd

def test_run(in_filename, out_filename,axs):
    try:
        arr = img_utils.read_image(in_filename)
    except (RuntimeError, TypeError, NameError,ValueError):
    #print("Oops!  That was no valid number.  Try again...")
        sys.exit()

def to_blocks():
    width, height = image.shape

# for image with ie. `RGB` color (3 bytes in every pixel)
#width, height, depth = image.shape 

    blocks = []

    for y in range(0, height, 4):
        for x in range(0, width, 4):
            blocks.append(image[y:y+4, x:x+4])
        