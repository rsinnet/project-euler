#!/usr/bin/python

i = 1000
a = 2**i
b = sum([int(x) for x in str(a)])
print 'i={}: {}'.format(i, b)
