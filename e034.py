#!/usr/bin/python

import math 

acc = 0
for i in xrange(3, 50000):
    msum = sum((math.factorial(int(x)) for x in list(str(i))))
    if msum == i:
        acc += i
print acc

