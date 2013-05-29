#!/usr/bin/python

import math 


dump = [0] * 10000000

def fac(n):
    if dump[n]:
        return dump[n]

    s = sum((int(x) ** 2 for x in list(str(n))))
    dump[n] = s
    return s

chain = {}

def fchain(n):
    
    if n == 1:
        return 1
    if n == 89:
        return 89

    if chain[n]:
        return chain[n]

    nxt = fac(n)
    s = fchain(nxt)

    chain[n] = s
    return s

def mnext(n):
    if n in chain:
        return chain[n]

    return fac(n)


acc = 0
for i in xrange(1, 10000000):
    nxt = mnext(i)
    while nxt != 1 and nxt != 89:
        nxt = mnext(nxt)
    chain[i] = nxt
    if nxt == 89:
        acc +=1

print acc
