#!/usr/bin/python

import math

def divcount(n):
    count = 0
    for x in xrange(1, int(math.sqrt(n)) + 1):
        if not n % x:
            count += 1
            if n / x != x:
                count += 1
    return count

acc = 0
for i in xrange(1, 20000):
    acc += i
    if divcount(acc) > 500:
        print acc
        break

