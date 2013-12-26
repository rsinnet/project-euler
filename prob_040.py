#!/usr/bin/python
# unsolved

a = ''

i = 1
while len(a) < 1000000:
    a += str(i)
    i += 1

print map(lambda x : int(a[10**x - 1]), range(7))
