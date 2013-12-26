#!/usr/bin/python

# Project Euler
# Problem 14
# Longest Collatz sequence

def get_sequence(x):
    i = 1
    while x != 1:
        i += 1
        if x % 2:
            x = 3 * x + 1
        else:
            x /= 2
    return i

N = int(1e6)

max_seq_len = 0
for i in range(2, N):
    foo = get_sequence(i)
    if foo > max_seq_len:
        max_seq_len = foo
        print i, foo
    if not i % (N / 25):
        print '[{}%]'.format(100 * i / N)
