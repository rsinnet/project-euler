#!/usr/bin/python

# Project Euler
# Problem 47
# Distinct prime factors

# About a minute runtime.

n = int(1e4)
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

N = 20
run_flag = True
num_factors = dict()
i = 2
M = 4

last_factors = [0] * M

while True:
    if not i % 10000:
        print i
    num_factors[i] = []
    a = i
    for j in foo:
        if j > i:
            break

        if not a % j:
            a /= j
            num_factors[i].append(j)
    last_factors[:-1] = last_factors[1:]
    last_factors[-1] = len(num_factors[i])
    if not any([v != M for v in last_factors]):
        break
    i+= 1

print i - M + 1
