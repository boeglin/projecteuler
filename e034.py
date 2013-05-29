#!/usr/bin/python

import math

def tolist(n):
    pos = int(math.log10(n))

    while pos >= 0:
        div = 10 ** pos
        yield math.factorial(n / div)
        n = n % div
        pos -= 1

acc = 0
for i in xrange(3, 50000):
    msum = sum(tolist(i))
    if msum == i:
        acc += i
print acc

