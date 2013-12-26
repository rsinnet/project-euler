#!/usr/bin/python
#unsolved

k = 5

#factorization
def get_factors(n):
    divs = [];
    for i in range(1, n+1):
        if not n % i:
            divs.append(i)

    return divs

def fx(x, a):
    return sum(map(lambda n : a[k-1-n] * x**n, range(k)))

# select a final number
# enumerate all possible rational roots
# iterate through all possible permutations

# 1. Find all possible solutions with rational roots theorem.
print get_factors(35)

a = [1, -2, -1, 2, 2]

print fx(-1, a)

# 2. Sort roots in ascending order.

# 3. Test roots in order. Break if condition 2 is not satisfied.
