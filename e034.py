#!/usr/bin/python

import math 

acc = 0
for i in xrange(3, 200000):
    l = [math.factorial(int(x)) for x in list(str(i))]
    msum = reduce(lambda x, y: x + y, l)
    if msum == i:
        print i
        acc += i
print acc

