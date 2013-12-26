#!/usr/bin/python
# run time on order of 10e0 minutes

import math

n = int(1e6)
i = 2

comp_nums = [False] * n
while i <= n / 2:
    if not comp_nums[i-1]:
        for x in range(2*i, n+1, i):
            comp_nums[x-1] = True
    i += 1

#print len([j+1 for j, y in enumerate(comp_nums) if not y])
foo = [j+1 for j, y in enumerate(comp_nums) if not y and j+1 > 1]

# foo contains all primes below n, inclusive

for i in range(len(foo)):
    run_flag = True
    cum_sum = 0
    j = 0
    while cum_sum < n:
        j = j + 1
        cum_sum += foo[i]


# find all primes up to 500,000
max_consec = 0
max_num = 0

for i in range(len(foo)):
    for j in range(i, len(foo)):
        bar = sum(foo[i:j])
        if bar > n:
            continue
        if not comp_nums[bar - 1]:
            if j-i > max_consec:
                max_consec = j-i
                max_num = bar
                print max_consec, max_num
