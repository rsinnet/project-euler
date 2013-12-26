#!/usr/bin/python

# Project Euler
# Problem 15
# Lattice paths

from math import factorial as f

def C(n, k):
    return f(n) / (f(k) * f(n - k))

N = 20

print sum([C(i+(N-1), i) for i in range(N+1)])

# Also, the answer is apparently 2N choose N.
