#!/usr/bin/python

# Project Euler
# Problem 89
# Roman numerals

roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

rback = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 90: 'XC',
         100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}

roman_desc = ['M', 'D', 'C', 'L', 'X', 'V', 'I']

def roman_to_int(s):
    l = len(s)
    cum_sum = 0
    i = 0
    while i < l:
        c = s[i]
        if i < l - 1:
            cn = s[i+1]
            if roman[cn] <= roman[c]:
                cum_sum += roman[c]
            else:
                cum_sum += roman[cn] - roman[c]
                i += 1
                if i == l:
                    break
        else:
            cum_sum += roman[c]
        i += 1
    return cum_sum

def int_to_min_roman(x):
    s = ''
    for y, r in sorted(rback.iteritems(), reverse=True):
        z = x / y
        if z > 0:
            x -= z * y
            s+= ''.join([rback[y]] * z)
            #print x, y, z, s
    return s

ochar = 0
nchar = 0
with open('roman.txt', 'rb') as file:
    for line in file:

        number = line.strip()
        baz = roman_to_int(number)
        bar = int_to_min_roman(baz)
        print baz, number, bar, len(number) - len(bar)

        ochar += len(number)
        nchar += len(int_to_min_roman(roman_to_int(number)))

print ochar - nchar
