#!/usr/bin/python

import csv

with open('names.txt', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in spamreader:

        foo = sorted(row)
        values = [0] * len(foo)
        for i in range(len(foo)):
            for c in foo[i]:
                values[i] += ord(c) - (ord('A') - 1)
            values[i] *= (i+1)
print sum(values)
