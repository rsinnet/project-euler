#!/usr/bin/python

# Project Euler
# Problem 37
# Truncatable primes

from math import log10

n=int(1e6)
i = 2

comp_nums = [False] * n
while i <= n / 2:
    if not comp_nums[i-1]:
        for x in range(2*i, n+1, i):
            comp_nums[x-1] = True
    i += 1

foo = [j+1 for j, y in enumerate(comp_nums) if not y and j+1 > 1]
#print foo

comp_nums[0] = True


def is_truncatable(x):
    s = str(x)
    l = int(log10(x)) + 1
    #print 'length: {}'.format(l)
    if comp_nums[x - 1]:
        return False

    for i in range(1, l):
        #print s[i:]
        if comp_nums[int(s[i:]) - 1]:
            return False

    for i in range(1, l):
        #print s[:-i]
        if comp_nums[int(s[:-i]) - 1]:
            return False

    return True

t_primes = []

for x in foo:
    if x < 10:
        continue

    if is_truncatable(x):
        t_primes.append(x)
        print x
print t_primes

print 'Sum = {}.'.format(sum(t_primes))
