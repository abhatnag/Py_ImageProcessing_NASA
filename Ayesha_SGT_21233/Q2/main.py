#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 09:11:12 2019

@author: ayeshabhatnagar
"""


# A function to check for valid inputs 
def isNumericChar(x): 
	if (x >= '0' and x <= '9'): 
		return True
	return False

# A simple atoi() function. If the given string contains 
# any invalid character, then this function returns 0 
def stringToInt(string): 
    #Discard all leading whitespaces
    string = string.lstrip()
    if len(string) == 0: 
        return 0
    res = 0
	# initialize as positive
    pos = 1
    i = 0

	# if number is negative then update sign 
    if string[0] == '-': 
        pos = -1
        i+=1

	# Iterate through the characters and update result
    for j in range(i,len(string)): 
        if isNumericChar(string[j] == False):
            return 0
        res = res*10 + (ord(string[j]) - ord('0')) 
        return pos*res 

def main():
    my_inp = "-1234675765756"
    print(stringToInt(my_inp))

if __name__ == '__main__':
    main()