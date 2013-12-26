#!/usr/bin/python
#unsolved

import itertools

n = 10000
i = 2

comp_nums = [False] * n
for j in range(i-1):
    comp_nums[j] = True

while i <= n / 2:
    if not comp_nums[i-1]:
        for x in range(2*i, n+1, i):
            comp_nums[x-1] = True
    i += 1
foo = [j+1 for j, y in enumerate(comp_nums) if not y and j+1 >= 1000]

bar = dict()

biglist = []

for i in range(len(foo)):
    if foo[i] in biglist:
        continue

    bar[foo[i]] = []
    gah = [int(''.join(x)) for x in list(itertools.permutations(str(foo[i])))]
    for z in gah:
        if not comp_nums[z-1] and z >= 1000:
            bar[foo[i]].append(z)
            biglist.append(z)
    bar[foo[i]] = list(set(bar[foo[i]]))

baf = dict()
for x, l in bar.iteritems():
    if len(l) > 2:
        print x, l
        baf[x] = l

print
print

# Iterate through each element in the dict and do subtraction
baz = dict()
for x, l in baf.iteritems():
    baz[x] = []
    for a in range(len(l)):
        if a == len(l) - 1:
            continue
        for b in range(a+1, len(l)):
            baz[x].append(abs(l[a] - l[b]))

    #if len(baz[x]) != len(set(baz[x])):
    #    print x, baz[x]


for x, l in baz.iteritems():
    for y in list(set(baz[x])):
        baz[x].remove(y)

for x, l in baz.iteritems():
    if len(l) > 0:
        print x, l


"""
# Iterate through each element in the dict and do subtraction
baz = dict()
for x, l in bar.iteritems():
    baz[x] = []
    for a in range(len(l)):
        if a == len(l) - 1:
            continue
        for b in range(a+1, len(l)):
            baz[x].append(abs(l[a] - l[b]))

    if len(baz[x]) != len(set(baz[x])) and len(baz[x]) > 0:
        print x, baz[x]

wag = dict()
for x, l in baz.items():
    if len(l) > 0 and 3330 in l:
        wag[x] = l

print wag

print bar[2699]
"""
