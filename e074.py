#!/usr/bin/python

import math 


dump = {}

def fac(n):
    if n in dump:
        return dump[n]

    s = sum((math.factorial(int(x)) for x in list(str(n))))
    dump[n] = s
    return s

chain = {}

k = -1
ks = 0

def fchain(l, n):
    global k, ks
    if n in chain:
        return chain[n]

    if n in l:
        k = n
        ks = len(l) - l.index(n)
        return ks

    l.append(n)
    nxt = fac(n)

    s = fchain(l[:], nxt) + 1
    if k in l:
        chain[n] = ks
        return ks
    else:
        k = -1

    chain[n] = s
    return s

print fchain([], 169), fchain([], 69)
print chain

acc = 0
for i in xrange(1, 1000000):
    l = fchain([], i)
    if l >= 60:
        acc += 1
        print l, acc, i

