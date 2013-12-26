#!/usr/bin/python

# Project Euler
# Problem 27
# Quadratic primes

n = int(1e6)
i = 2

comp_nums = [False] * n
while i <= n / 2:
    if not comp_nums[i-1]:
        for x in range(2*i, n+1, i):
            comp_nums[x-1] = True
    i += 1

N = 1000

max_consec = 0
max_a = 10000
max_b = 10000
for a in range(-N, N+1):
    for b in range(-N, N+1):
        n = 0
        while True:
            foo = n**2 + a * n + b
            if foo <= 1 or comp_nums[foo-1]:
                break

            n += 1

            if n > max_consec:
                max_consec = n
                max_a = a
                max_b = b

print 'n={}, a={}, b={}, ab={}'.format(max_consec, max_a, max_b, max_a * max_b)
