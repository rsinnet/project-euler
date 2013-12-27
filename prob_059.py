#!/usr/bin/python

# Project Euler
# Problem 59
# XOR decryption

import csv
import itertools
import string

lookstring = ' the '
keylen = 3
keys = list(itertools.product('abcdefghijklmnopqrstuvwxyz', repeat=keylen))
print len(keys)

with open('cipher1.txt', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    for row in spamreader:
        testnum = 0
        for key in keys:
            testnum += 1
            if not testnum % 500:
                print '{}%'.format(testnum / float(len(keys)) * 100)
            foo = ''
            for i in range(len(row)):
                foo += chr(ord(key[i % keylen]) ^  int(row[i]))
            if string.find(foo, lookstring) >= 0:
                ans = sum([ord(j) for j in foo])
                print '{}, ans={}: {}'.format(key, ans, foo)
