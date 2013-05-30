#!/usr/bin/python

import math

def tolist(n):
    while n:
        yield math.factorial(n % 10)
        n /= 10

acc = 0
for i in xrange(3, 50000):
    msum = sum(tolist(i))
    if msum == i:
        acc += i
print acc

