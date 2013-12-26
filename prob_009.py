#!/usr/bin/python

# Project Euler
# Problem 9
# Special Pythagorean triplet

for a in range(1, 1001):
    for b in range(a, 1001):
        c = 1000 - a - b
        if c**2 == a**2 + b**2:
            print 'a={}, b={}, c={}, abc={}'.format(a, b, c, a*b*c)
