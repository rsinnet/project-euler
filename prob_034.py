#!/usr/bin/python

import math

a = []
for i in range(10,1500000):
    cum_sum = 0
    for j in str(i):
        cum_sum += math.factorial(int(j))
    if cum_sum == i:
        a.append(i)
        print a
print sum(a)
