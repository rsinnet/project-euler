#!/usr/bin/python

penult_fib = 1
last_fib = 1

i = 2
while len(str(last_fib)) < 1000:
    foo = last_fib
    last_fib = penult_fib + last_fib
    penult_fib = foo
    i += 1
    #print "i={}, fib={}".format(i, last_fib)
print i
