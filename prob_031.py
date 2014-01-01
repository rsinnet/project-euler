#!/usr/bin/python

# Project Euler
# Problem 31
# Coin sums

coins = [200, 100, 50, 20, 10, 5, 2, 1]
M = 200

ways = [0] * (M+1)
ways[0] = 1
for i in range(len(coins)):
    for j in range(coins[i], M+1):
        ways[j] += ways[j - coins[i]]
print ways[-1]
