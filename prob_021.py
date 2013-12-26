#!/usr/bin/python

import math

# played around with n by hand until length was 10002
n=10000
i = 2

a = []

# factorization
def get_factors(n):
    divs = [];
    for i in range(1, n+1):
        if not n % i:
            divs.append(i)

    return divs

for i in range(1,10001):
    foo = get_factors(i)
    bar = sum(foo[:-1])
    j = sum(get_factors(bar)[:-1])
    if i == j and i != bar:
        print foo[:-1]
        print get_factors(bar)[:-1]
        print i, bar
        a.append(i)

print sum(a)

