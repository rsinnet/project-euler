#!/usr/bin/python

numwords = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
            6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
            11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
            15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen',
            19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty',
            50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety',
            1000: 'onethousand'}

for i in range(1,10):
    numwords[100*i] = numwords[i] + 'hundred'

for i in range(2,10):
    for j in range(1,10):
        numwords[10*i+j] = numwords[10*i] + numwords[j]

for i in range(1,10):
    for j in range(1,100):
        numwords[100*i+j] = numwords[100*i] + 'and' + numwords[j]

cum_sum = 0
for i in range(1,1001):
    cum_sum += len(numwords[i])

print numwords

print cum_sum

print len(numwords[115])
print len(numwords[342])
