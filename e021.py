#!/usr/bin/python

import math

back = {}
def div(n):
    if n in back:
        return back[n]

    acc = 0
    for x in xrange(1, int(math.sqrt(n)) + 1):
        if not n % x:
            acc += x
            if acc / x != x: # only add root square once
                acc += n / x
    back[n] = acc
    return acc

acc = 0
for i in xrange(1, 10000):
    ami = div(i)
    if i != ami and i == div(ami):
        acc += i
print acc
