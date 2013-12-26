#!/usr/bin/python

import math

# played around with n by hand until length was 10002
n=2000000
i = 2

comp_nums = [False] * n
while i <= n / 2:
    if not comp_nums[i-1]:
        for x in range(2*i, n+1, i):
            comp_nums[x-1] = True
    i += 1

print sum([j+1 for j, y in enumerate(comp_nums) if not y]) - 1
