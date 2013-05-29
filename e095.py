#!/usr/bin/python

import math

back = {}

def div(n):
    acc = 0

    if n in back:
        return back[n]

    for x in xrange(1, int(math.sqrt(n)) + 1):
        if not n % x:
            acc += x
            if acc / x != x:
                acc += n / x
    back[n] = acc
    return acc

def chain(n):
    l = [n]
    ami = div(n)
    while ami < 999999 and ami not in l:
        l.append(ami)
        ami = div(ami)
    if ami == n:
        return (len(l), l)
    return (0, [])

maxi = 0
l = []

for i in xrange(3, 15000):
    res = chain(i)
    if res[0] > maxi:
        maxi, l = res
        print maxi, reduce(min, l)
