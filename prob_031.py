#!/usr/bin/python

# Project Euler
# Problem 31
# Coin sums

coins = [200, 100, 50, 20, 10, 5, 2, 1]
i = 0
M = 200

for a0 in range(M, -1, -coins[0]):
    for a1 in range(a0, -1, -coins[1]):
        for a2 in range(a1, -1, -coins[2]):
            for a3 in range(a2, -1, -coins[3]):
                for a4 in range(a3, -1, -coins[4]):
                    for a5 in range(a4, -1, -coins[5]):
                        for a6 in range(a5, -1, -coins[6]):
                            i += 1
print i
