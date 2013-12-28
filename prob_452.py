#!/usr/bin/python

# Project Euler
# Problem 452
# Long Products

# unsolved

import itertools
from operator import mul

n = int(1e1)
m = int(1e1)

A = range(1, n + 1)
#
B = list(itertools.product(A, repeat=10))
print len(B)
#C = [1 for j in B if reduce(mul, B[0], 1) <= m]

print C
