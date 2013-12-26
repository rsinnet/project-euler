#!/usr/bin/python
n = 1000

p_sol = dict()

for p in range(3, n + 1):
    p_sol[p] = 0
    for a in range(1, p + 1):
        for b in range(a, p + 1):
            c = p - a - b
            if c**2 == a**2 + b**2:
                p_sol[p] += 1
    print p

max_v =  max(v for k, v in p_sol.iteritems())
print [k for k, v in p_sol.iteritems() if v == max_v]
