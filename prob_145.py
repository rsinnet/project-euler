#!/usr/bin/python

# Project Euler
# Problem 145
# How many reversible numbers are there below one-billion?

# Final solution is 608720, only needs 9%.

from math import log10

def check_odd(x):
    s = str(x)
    for c in s:
        if not int(c) % 2:
            return False
    return True

I = int(1e9)

last_accum = 0
accum = 0
i = 0
while i < I:
    i += 1
    if not i % (I/1000):
        print 'i={}%: accum: {}, diff: {}'.format(100*float(i) / I, accum, \
                                            accum - last_accum)
        last_accum = accum

    rev_i = int(str(i)[::-1])
    if int(log10(i)) != int(log10(rev_i)):
        continue
    num = i + rev_i
    foo = check_odd(num)
    if foo:
        accum += 1

print accum
