#!/usr/bin/python

a = []
for i in range(2,1000000):
    cum_sum = 0
    for j in str(i):
        cum_sum += int(j)**5
    if cum_sum == i:
        a.append(i)
        print a
print sum(a)
