#!/usr/bin/python
#unsolved

import math

n=1000000
i = 2

comp_nums = [False] * n
while i <= n / 2:
    if not comp_nums[i-1]:
        for x in range(2*i, n+1, i):
            comp_nums[x-1] = True
    i += 1

print len([j+1 for j, y in enumerate(comp_nums) if not y])
foo = [j+1 for j, y in enumerate(comp_nums) if not y]


def rotate_left(s):
    return s[-1] + s[0:-1]

foo_good = [True] * n

for j in range(2,n):
    baz = str(j)
    for k in range(len(baz)):
        baz = rotate_left(baz)
        if comp_nums[int(baz) - 1]:
            foo_good[j] = False

print len([j for j, y in enumerate(foo_good) if y and j > 1])
