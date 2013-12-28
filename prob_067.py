# Project Euler
# Problem 67
# Maximum path sum II

import numpy as np
import csv

t = []

with open('triangle.txt', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ')
    for row in spamreader:
        t.append([int(x) for x in row])

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
# Find longest path:
print max([v for k, v in y[-1].iteritems()])
