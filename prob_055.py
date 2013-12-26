#!/usr/bin/python

# Project Euler
# Problem 55
# Lychrel numbers

N = 10000
max_iter = 50

def is_palindrome(x):
    s = str(x)
    l = len(s) / 2
    if x < 10:
        return True
    return s[:l] == s[-l:][::-1]

cum_sum = 0

for x in range(N):
    y = x
    for i in range(max_iter):
        y += int(str(y)[::-1])

        if x == 4994:
            print y

        if is_palindrome(y):
            print '{} is a palindrome, goes to {}.'.format(x, y)
            break
        if i == max_iter - 1:
            cum_sum += 1
            print '{} is a Lychrel number.'.format(x)

print '{} Lychrel numbers.'.format(cum_sum)
