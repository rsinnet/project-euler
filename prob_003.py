#!/usr/bin/python

z = 600851475143
m = int(1e4)

i = 2

# Find all prime numbers up to ten thousand
comp_nums = [False] * m
while i <= m / 2:
    if not comp_nums[i-1]:
        for x in range(2*i, m+1, i):
            comp_nums[x-1] = True
    i += 1
foo = [j+1 for j, y in enumerate(comp_nums) if not y and j+1 > 1]

print 'Found primes up to ten thousand! Factoring...'

for x in foo:
    if not z % x:
        y = z / x
        print '{} / {} = {}'.format(z, x, y)
        z = y

if z == 1:
    print 'Factorized!'
