#!/usr/bin/python

# Project Euler
# Problem 23
# Non-abundant sums

N = 28123
abund_nums = [False] * N

# 1. Find all abundant numbers
def get_factors(n):
    divs = [];
    for i in range(1, n+1):
        if not n % i:
            divs.append(i)

    return divs[:-1]

for i in range(1,N):
    abund_nums[i] = sum(get_factors(i+1)) > i + 1
    if not i % 1000:
        print i

foo = [j+1 for j in range(len(abund_nums)) if abund_nums[j]]
print '{} abundant numbers less than {} found.'.format(len(foo), N)

#print foo

print

# 2. Loop through all abundant numbers for each in the above list and check if
# difference is in list.
no_sum = [True] * N
for i in range(N):
    for j in foo:
        if j >= i:
            break
        if abund_nums[(i+1) - j - 1]:
            no_sum[i] = False
            #print i+1, j, i+1 - j
            break

print sum([i+1 for i in range(len(no_sum)) if no_sum[i]])
