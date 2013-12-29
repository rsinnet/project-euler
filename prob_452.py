#!/usr/bin/python

# Project Euler
# Problem 452
# Long Products

# unsolved

import itertools
from operator import mul

"""
n=10000000
i = 2

comp_nums = [False] * n
while i <= n / 2:
    if not comp_nums[i-1]:
        for x in range(2*i, n+1, i):
            comp_nums[x-1] = True
    i += 1

print len([j+1 for j, y in enumerate(comp_nums) if not y])
foo = [j+1 for j, y in enumerate(comp_nums) if not y]
"""

n = 3
m = 3

A = range(1, n + 1)
B = itertools.product(A, repeat=n)

cum_sum = 0
for b in  B:
    if reduce(mul, b, 1) <= m:
        cum_sum += 1
        if not cum_sum % 10:
            print cum_sum

print cum_sum
