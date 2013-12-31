#!/usr/bin/python

# Project Euler
# Problem 97
# Large non-Mersenne prime

N = 7830457
i = 0
m = 28433
while i < N:
    m = m * 2 % 10000000000
    i += 1
    if not i % (N/25):
        print '{}%'.format(100*i / N)

print m+1
