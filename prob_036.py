#!/usr/bin/python

# Project Euler
# Problem 36
# Double-base palindromes

def is_palindrome(x):
    s = str(x)
    l = len(s) / 2
    if x < 10:
        return True
    return s[:l] == s[-l:][::-1]

n = 1
for i in range(1, 2**10+1, 2):
    s = '{0:b}'.format(i)
    for j in range(len(s), 11):
        s2 = '0' * (10 - j) + '{0:b}'.format(i)
        s3 = s2[::-1] + s2
        x = int(s3, 2)
        if is_palindrome(x) and x < 1000000:
            print s3, x
            n += x

    for k in [0, 1]:
        for j in range(len(s), 11):
            s2 = '0' * (10 - j) + '{0:b}'.format(i)
            s3 = s2[::-1] + str(k) + s2
            x = int(s3, 2)
            if is_palindrome(x) and x < 1000000:
                print s3, x
                n += x
print n
