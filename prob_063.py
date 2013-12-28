#!/usr/bin/python

# Project Euler
# Problem 63
# Powerful digit counts

k = 0
i = 1
while len(str(9**i)) == i:
    j = 9
    while len(str(j**i)) == i and j > 0:
        print 'i={}, j={}, j^i={}, N(j^i)={}'.format(i, j, j**i, len(str(j**i)))
        k += 1
        j -= 1
    i += 1

i -= 1
print i, k
