#!/usr/bin/python

import csv

j = 0
ts = map(lambda n : (n * (n + 1)) / 2, range(1, 100))

with open('words.txt', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in spamreader:

        values = [0] * len(row)
        for i in range(len(row)):
            for c in row[i]:
                values[i] += ord(c) - (ord('A') - 1)

            if any(item == values[i] for item in ts):
                j = j+1

print j
