# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2018-09-18 21:37:42
# @Last Modified by:   vu
# @Last Modified time: 2018-09-19 17:52:41


"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and 
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""

def binary_search(input_array, value):
    """Your code goes here."""
    lower = 0; upper = len(input_array);
    while lower <= upper:
    	i = int((lower + upper)/2)
    	if input_array[i] == value:
    		return i
    	elif input_array[i] > value:
    		upper = i-1
    	else:
    		lower = i+1
    return -1

test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print(binary_search(test_list, test_val1))
print(binary_search(test_list, test_val2))