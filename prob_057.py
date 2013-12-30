#!/usr/bin/python

# Project Euler
# Problem 57
# Square root convergents

from fractions import Fraction as F
from math import log10

N = 1000
x = 2 + F(1,2)
k = 0

for i in range(1, N+1):
    x = 2 + F(1,x)
    y = x-1
    if int(log10(y.numerator)) > int(log10(y.denominator)):
        k += 1

print k
