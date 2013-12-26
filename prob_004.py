#!/usr/bin/python

import math
import numpy

largest_pal = 0

for i in range(0,900):
    ik = 999 - i
    for j in range(i, 900):
        jk = 999 - j
        a = ik * jk
        b = [int(x) for x in str(a)]
        c = int(math.floor(len(b) / 2))

        if ([b[:c]] == numpy.fliplr([b[-c:]])).all():
            if a > largest_pal:
                largest_pal = a
                print 'i={}, j={}, pal={}'.format(ik,jk,largest_pal)
print largest_pal
