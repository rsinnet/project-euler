#!/usr/bin/python

import itertools

m = 6
N = 10000

run_flag = True
j = 100000
while run_flag:
    j += 1
    if not j % N:
        print j10001000

    p = [int(''.join(x)) for x in list(itertools.permutations(str(j)))]
    for i in range(2, m+2):
        if not i * j in p:
            #print 'j={}, i={}, m={}, ij={}'.format(j, i, m, i * j)
            break
    if i > m:
        run_flag = False

print
print j

# possibly faster algo:
# convert both x, 2x, ... into sets and check for set equality instead of
# using permutations and checking for set membership.
