#!/usr/bin/python

# Project Euler
# Problem 31
# Coin sums

# unsolved

coins = [200, 100, 50, 20, 10, 5, 2, 1]

i = 0

for a1 in range(200 / coins[1] + 1):
    bar = [0, a1, 0, 0, 0, 0, 0, 0]
    baz =  a1 * coins[1]
    if baz == 200:
        i += 1
        print i, bar, baz
        continue
    if baz > 200:
        continue

    for a2 in range(200 / coins[1]+1):
        bar = [0, a1, a2, 0, 0, 0, 0, 0]
        baz =  sum([bar[j] * coins[j] for j in range(1,3)])
        if baz == 200:
            i += 1
            print i, bar, baz
            continue
        if baz > 200:
            continue

        for a3 in range(200 / coins[3]+1):
            bar = [0, a1, a2, a3, 0, 0, 0, 0]
            baz =  sum([bar[j] * coins[j] for j in range(1,4)])
            if baz == 200:
                i += 1
                print i, bar, baz
                continue
            if baz > 200:
                continue

            for a4 in range(200 / coins[4] + 1):
                bar = [0, a1, a2, a3, a4, 0, 0, 0]
                baz =  sum([bar[j] * coins[j] for j in range(1,5)])
                if baz == 200:
                    i += 1
                    print i, bar, baz
                    continue
                if baz > 200:
                    continue

                for a5 in range(200 / coins[5] + 1):
                    bar = [0, a1, a2, a3, a4, a5, 0, 0]
                    baz =  sum([bar[j] * coins[j] for j in range(1,6)])
                    if baz == 200:
                        i += 1
                        print i, bar, baz
                        continue
                    if baz > 200:
                        continue

                    for a6 in range(200 / coins[6] + 1):
                        bar = [0, a1, a2, a3, a4, a5, a6, 0]
                        baz =  sum([bar[j] * coins[j] for j in range(1,7)])
                        if baz == 200:
                            i += 1
                            print i, bar, baz
                            continue
                        if baz > 200:
                            continue

                        for a7 in range(200 / coins[7] + 1):
                            bar = [0, a1, a2, a3, a4, a5, a6, a7]
                            baz =  sum([bar[j] * coins[j] for j in range(1,8)])
                            if baz == 200:
                                i += 1
                                print i, bar, baz
                                continue
                            if baz > 200:
                                continue
i += 1
print i, [1, 0, 0, 0, 0, 0, 0, 0], 200

print i
