#!/usr/bin/python

i = 0

coins = [200, 100, 50, 20, 10, 5, 2, 1]

def add_coin(tot, k):
    global i
    if tot == 200:
        i += 1

    if tot >= 200:
        return

    else:
        for c in coins:
            if tot + c <= 200:
                add_coin(tot + c, k +1)

add_coin(0, 0)
print i
