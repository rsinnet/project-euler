#!/usr/bin/python

# Project Euler
# Problem 28
# Number spiral diagonals

cum_sum = 1
last = 1
for x in [range((i-1), (i-1)*5, i-1) for i in range(3, 1003, 2)]:
    baz = [y + last for y in x]
    cum_sum += sum(baz)
    last = baz[-1]
print cum_sum
