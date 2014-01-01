#!/usr/bin/python

# Project Euler
# Problem 46
# Goldbach's other conjecture

n = int(1e6)
i = 2

comp_nums = [False] * n
while i <= n / 2:
    if not comp_nums[i-1]:
        for x in range(2*i, n+1, i):
            comp_nums[x-1] = True
    i += 1

foo = [j+1 for j, y in enumerate(comp_nums) if not y and j+1 > 2]


for i in range(5, 10001, 2):
    j = 0
    if not comp_nums[i-1]:
        continue
    while True:
        j += 1
        x = i - 2*j**2
        if x < 2:
            break
        if not comp_nums[x-1]:
            break

    print '{} = {} + 2 * {}^2'.format(i, x, j)
        
    if x < 2:
        break
print
print '{} = {} + 2 * {}^2'.format(i, x, j)
