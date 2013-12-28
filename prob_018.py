#!/usr/bin/python

# Project Euler
# Problem 18
# Maximum path sum I

import numpy as np

t = [[75],
     [95, 64],
     [17, 47, 82],
     [18, 35, 87, 10],
     [20, 4, 82, 47, 65],
     [19, 1, 23, 75, 3, 34],
     [88, 2, 77, 73, 7, 63, 67],
     [99, 65, 4, 28, 6, 16, 70, 92],
     [41, 41, 26, 56, 83, 40, 80, 70, 33],
     [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
     [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
     [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
     [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
     [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
     [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]]
y = [{0: t[0][0]}]
sum_paths = [{0: [0]}]
for i in range(1, len(t)):
    l = len(t[i])
    x = np.arange(-l+1, l+1, 2)
    y.append(dict())
    sum_paths.append(dict())
    for j in range(len(x)):
        y[i][x[j]] = t[i][j]
        max_last = 0
        for k in [-1, 1]:
            try:
                foo = y[i-1][x[j] + k]
                if foo > max_last:
                    max_last = foo
                    last_path = sum_paths[i-1][x[j] + k]
            except KeyError:
                pass
        y[i][x[j]] += max_last
        sum_paths[i][x[j]] = last_path + [x[j]]
print
print y

print
print sum_paths

print
# Find longest path:
print max([v for k, v in y[-1].iteritems()])
