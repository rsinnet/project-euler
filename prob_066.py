#!/usr/bin/python

# Project Euler
# Problem 66
# Diophantine equation

# unsolved

from math import sqrt as s

N = 1000

max_x = 0
max_D = 0

def Dio(D, x, y):
    return x**2 - D * y**2

for D in range(2, N + 1):
    foo = s(D)
    if int(foo) == foo:
        continue

    x = 2
    while True:
        y2 = (x**2 - 1.) / D
        y = s(y2)
        if abs(int(y) - y) < 1e-8:
            #print x, y, D, int(s(y2)) == s(y2)

            #print "{1}^2 - {0} * {2}^2 == 1".format(D, x, int(y))
            if max_x < x:
                max_x = x
                max_D = D
                print '---- max_x={}, max_D={}, Dio={}'.format(x, D, Dio(D, x, int(y)))
            break
        x += 1

print max_D, max_x
