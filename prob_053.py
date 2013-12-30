#!/usr/bin/python

# Project Euler
# Problem 53
# Combinatoric selections

from scipy.misc import comb as C

N = 0
print 
for n in range(23, 101):
    for i in range(4, 50):
        if C(n, i) > 1000000:
            print '{}: {}'.format(n, (n - 2*i) + 1)
            N += n - 2*i + 1
            break

print
print '1 <= n <= 100: {}'.format(N)
