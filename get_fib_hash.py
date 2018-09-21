# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2018-09-20 05:32:32
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2018-09-20 13:35:25

"""
Hash version of get_fibo.
Time execution is very impressive.
"""

"""Implement a function recursively to get the desired
Fibonacci sequence value.
Your code should have the same input/output as the 
iterative code in the instructions."""

hash_table = {0:0, 1:1}

def get_fib_hash(position):
    if position in hash_table:
        return hash_table[position]
    v = get_fib_hash(position-2) + get_fib_hash(position-1)
    hash_table[position] = v
    return hash_table[position]

# Test cases
print(get_fib_hash(9))
print(get_fib_hash(11))
print(get_fib_hash(0))

# Time execution
import time
start_time = time.time()
n = 35
print("get_fib_hash(%d) = %d" % (n, get_fib_hash(n)))
end_time = time.time()
print("Time execution (in seconds) of get_fib_hash(%d) is %s" % (n, (end_time - start_time)))