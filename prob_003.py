#!/usr/bin/python
#unsolved

import math

z = 600851475143
n = int(math.sqrt(z))
i = 2

comp_nums = [False] * n
while i <= n / 2:
    if not comp_nums[i-1]:
        for x in range(2*i, n+1, i):
            comp_nums[x-1] = True
    i += 1
print [j+1 for j, y in enumerate(comp_nums) if not y]
