#!/usr/bin/python

import math

def tolist(n):
    while n:
        yield math.factorial(n % 10)
        n /= 10

chain = {}
def fchain(n):
    l = []
    nxt = n
    while nxt not in l and nxt not in chain:
        l.append(nxt)
        nxt = sum(tolist(nxt))

    if nxt in l: # out of cache chain ended in loop
        idx = l.index(nxt)
        c_len = len(l) - idx
        for i in l[idx:]:
            chain[i] = c_len

        if idx > 0:
            for i in l[idx - 1::-1]:
                c_len += 1
                chain[i] = c_len
    elif l: # cache hit after a while
        c_len = chain[nxt]
        for i in l[::-1]:
            c_len += 1
            chain[i] = c_len
    return chain[n]

acc = 0
for i in xrange(1, 1000000):
    l = fchain(i)
    if l == 60:
        acc += 1
print acc

