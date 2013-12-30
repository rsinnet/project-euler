#!/usr/bin/python

# Project Euler
# Problem 41
# Pandigital prime

from itertools import permutations as P
from fractions import gcd
from math import sqrt as s

N = 7

foo = P(range(1, N+1), N)
n = 0
for p in reversed(list(foo)):
    x = sum([10**(len(p)-k-1) * p[k] for k in range(len(p))])
    n += 1

    if not n % 1000:
        print n, x

    is_prime = True
    for i in range(2, int(s(x))+1):
        if not x % i:
            is_prime = False
            break

    if is_prime:
        print "answer: {}".format(x)
        break

print n, x
