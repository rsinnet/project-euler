#!/usr/bin/python

# Project Euler
# Problem 76
# Counting summations

M = 100
ints = range(1, M+1)

ways = [0] * (M+1)
ways[0] = 1
for i in range(0,len(ints)-1):
    for j in range(ints[i], M+1):
        ways[j] += ways[j - ints[i]]
print ways[-1]
