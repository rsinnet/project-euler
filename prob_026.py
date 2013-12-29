#!/usr/bin/python

# Project Euler
# Problem 26
# Reciprocal cycles

import itertools
from operator import mul

n=1000
i = 2

comp_nums = [False] * n
while i <= n / 2:
    if not comp_nums[i-1]:
        for x in range(2*i, n+1, i):
            comp_nums[x-1] = True
    i += 1

print len([j+1 for j, y in enumerate(comp_nums) if not y and j+1 > 2])
foo = [j+1 for j, y in enumerate(comp_nums) if not y and j+1 > 2]
print foo[:5], foo[-5:]
max_cycle = 0
max_num = 0

for x in foo:
    k = 1
    R = 10 % x

    if not R:
        continue

    while R != 1:
        #print '{} * {} % {} = {}'.format(R, 10, x, R * 10 % x) 
        R = R * 10 % x
        k += 1
    if k > max_cycle:
        max_cycle = k
        max_num = x
        print max_num, max_cycle

