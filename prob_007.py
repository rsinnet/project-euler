#!/usr/bin/python
#unsolved

import math

# played around with n by hand until length was 10002
n=104750
i = 2

comp_nums = [False] * n
while i <= n / 2:
    if not comp_nums[i-1]:
        for x in range(2*i, n+1, i):
            comp_nums[x-1] = True
    i += 1

print len([j+1 for j, y in enumerate(comp_nums) if not y])
print [j+1 for j, y in enumerate(comp_nums) if not y]
