#!/usr/bin/python
#unsolved
# should use recursion

import math

n = int(1e3)
i = 2

comp_nums = [False] * n
while i <= n / 2:
    if not comp_nums[i-1]:
        for x in range(2*i, n+1, i):
            comp_nums[x-1] = True
    i += 1

print len([j+1 for j, y in enumerate(comp_nums) if not y])
foo = [j+1 for j, y in enumerate(comp_nums) if not y]

# foo contains all primes below 1e6

for i in range(len(foo)):
    run_flag = True
    cum_sum = 0
    j = 0
    while cum_sum < n:
        j = j + 1
        cum_sum += foo[i]

