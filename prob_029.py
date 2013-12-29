#!/usr/bin/python
# Project Euler
# Problem 29
# Distinct powers

# unsolved

import itertools

N = 100

A = set()
for a in range(2, N+1):
    for b in range(2, N+1):
        #print a, b
        A.add(a**b)
print len(A)
