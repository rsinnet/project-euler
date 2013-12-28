#!/usr/bin/python

# Project Euler
# Problem 69
# Totient maximum

from fractions import gcd
N = int(1e3)

# Answer only depends on number of primes:
# 2 * 3 * 5 * 7 * 11 * 13 * 17

t_max = [1] * N

for i in range(2, N):
    if not i % (N / 10):
        print '{}%'.format(100 * i / N)
    for j in range(2, i):
        if gcd(i, j) == 1:
            t_max[i] += 1
    t_max[i] = float(i) / t_max[i]

print t_max.index(max(t_max)), max(t_max)
