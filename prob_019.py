#!/usr/bin/python

# Project Euler
# Problem 19
# Counting Sundays

import numpy

no_leap  = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
yes_leap = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

leaps = []

day0 = 1 # monday
days = 0
first_month_days = []

for i in range(1900, 2001):

    if not i % 4 and (i % 100 or not i % 400):
        leaps.append(i)
        ld = yes_leap
    else:
        ld = no_leap

    print i, sum(ld)
    first_month_days.append([sum(ld[:k]) + days for k in range(len(ld)+1)])
    days += sum(ld)

z = numpy.array(first_month_days).flatten()
print z[-1]+1

y = set(z)
w = set([x + 6 for x in range(0, z[-1]+1, 7)])
q = [x for x in y.intersection(w) if x >= sum(no_leap)]

#print [x - sum(no_leap) for x in q]
print len(q)
