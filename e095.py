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

chain = {} # contains (len, min)
def fchain(n):
    if n in chain:
        return chain[n]

    l = [n]
    ami = div(n)
    while ami < 999999 and ami not in l and ami not in chain:
        l.append(ami)
        ami = div(ami)
    if ami == n: # is an amicable chain
        ret = (len(l), min(l))
        for i in l:
            chain[i] = ret
        return ret
    elif ami > 999999: # leads to a crash
        for i in l:
            chain[i] = (0, 0)
    elif ami in chain: # leads to something known, l is not amicable
        for i in l:
            chain[i] = (0, 0)
    elif ami in l: # part of l is amicable
        idx = l.index(ami)
        for i in l[:idx]:
            chain[i] = (0, 0)
        ll = l[idx:]
        ret = (len(ll), min(ll))
        for i in ll:
            chain[i] = ret
    return (0, 0)

maxi = 0
elem = 0

for i in xrange(1, 1000000):
    res = fchain(i)
    if res[0] > maxi or (res[0] == maxi and res[1] < elem):
        maxi, elem = res
print elem
