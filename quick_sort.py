# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2018-09-21 16:29:34
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2018-09-21 16:42:37

"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
def quicksort(array):
    n = len(array)
    if n <= 1:
        return array

    pivot = n-1 # choose pivot

    # partition
    j = 0
    while (j < pivot):
        if array[j] > array[pivot]: # shift & swap
            array[j:pivot+1] = array[j+1:pivot] + [array[pivot], array[j]]
            pivot -= 1; j -= 1
        j += 1
    
    # recursively sort left and right parts
    array[:pivot] = quicksort(array[:pivot])
    array[pivot+1:] = quicksort(array[pivot+1:])
    return array
    
test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print('input array: ' + str(test))
print('output array: ' + str(quicksort(test)))