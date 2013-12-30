#!/usr/bin/python

# Project Euler
# Problem 45
# Triangular, pentagonal, and hexagonal

T = [n*(n+1) / 2 for n in range(1,60000)]
P = [n*(3*n-1) / 2 for n in range(1,60000)]
H = [n*(2*n-1) for n in range(1,30000)]

for h in H:
    if h == 1:
        continue
    if h in P:
        if h in T:
            if h == 40755:
                continue
            print T.index(h)+1, h
            break
