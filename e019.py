#!/usr/bin/python

acc = 0
d = 0

for y in xrange(1900, 2001):
    for m in xrange(1, 13):
        if y > 1900:
            if d % 7 == 6:
                acc += 1
        if m in [1, 3, 5, 7, 8, 10, 12]:
            d += 31
        elif m in [4, 6, 9, 11]:
            d += 30
        elif (not m % 4) and ((not m % 400) or (m % 100)):
            d += 29
        else:
            d += 28

print acc

