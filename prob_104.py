#!/usr/bin/python

# Project Euler
# Problem 104
# Pandigital Fibonacci ends

def is_pandigital(x):
    digits = [0] * 9
    for c in str(x):
        digits[int(c)-1] = 1
    return sum(digits) == 9

k = 3
fib = [2L, 1L]
while True:
    k += 1
    foo = sum(fib) % 1000000000
    fib[1] = fib[0]
    fib[0] = foo

    if foo >= 100000000:
        baz = str(foo)
        if is_pandigital(baz):
            bar = k * 0.20898764024997873 - 0.3494850021680094
            if is_pandigital(str(int( pow(10, bar - int(bar) + 8 ) ))):
                break
        if not k % 1000:
            print k

print 'answer: {}'.format(k)
