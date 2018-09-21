# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2018-09-20 04:59:57
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2018-09-20 13:34:43

"""Implement a function recursively to get the desired
Fibonacci sequence value.
Your code should have the same input/output as the 
iterative code in the instructions."""

def get_fib(position):
    if position <= 1:
        return position
    return get_fib(position-2) + get_fib(position-1)

# Test cases
print(get_fib(9))
print(get_fib(11))
print(get_fib(0))

# Time execution
import time
start_time = time.time()
n = 35
print("get_fib(%d) = %d" % (n, get_fib(n)))
end_time = time.time()
print("Time execution (in seconds) of get_fib(%d) is %s" % (n, (end_time - start_time)))