#!/usr/bin/python

# Project Euler
# Problem 79
# Passcode derivation

num = dict()

with open('keylog.txt', 'rb') as file:
    for row in file:
        foo = row.strip()

        for i in range(len(foo)):
            x = int(foo[i])
            if not x in num:
                num[x] = {'left': set(), 'right': set()}
            #print x, [int(c) for c in foo[:i]], [int(c) for c in foo[i+1:]]
            num[x]['left'] = \
                num[x]['left'].union(set([int(c) for c in foo[:i]]))
            num[x]['right'] = \
                num[x]['right'].union(set([int(c) for c in foo[i+1:]]))

for k, v in num.iteritems():
    print k, v
