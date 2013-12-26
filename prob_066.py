#!/usr/bin/python

# Project Euler
# Problem 66
# Diophantine equation

# unsolved

from math import sqrt as s

N = 100

max_x = 0
max_D = 0

def Dio(D, x, y):
    return x**2 - D * y**2

for D in range(1, N + 1):
    foo = s(D)
    if int(foo) == foo:
        continue
    run_flag = True
    x = 1

    while run_flag:
        y = 1
        while run_flag:
            foo = Dio(D, x, y)
            run_flag = not foo == 1
            if not run_flag:
                print "{1}^2 - {0} * {2}^2 == 1".format(D, x, y)
                if max_x < x:
                    max_x = x
                    max_D = D
                    print 'max_x={}, max_D={}'.format(x, D)
            y += 1
            if foo < 1:
                break;
        x += 1
