#!/usr/bin/python

# Project Euler
# Problem 12
# Highly divisible triangular number

# Around 24 hours runtime, very inefficient

n = 0
m = 1

go_flag = True

while go_flag:

    n += m

    divs = [];
    for i in range(1, n+1):
        if not n % i:
            divs.append(i)


    print 'm={}, n={}, n_factors: {}'.format(m, n, len(divs))

    if len(divs) > 500:
        go_flag = False

    m += 1

