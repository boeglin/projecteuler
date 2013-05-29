#!/usr/bin/python

import sys, math

def perm(pre, l):
    if len(l) == 1:
        return [pre + str(l[0])]

    ret = []
    for i in l:
        m = l[:]
        m.remove(i)
        ret.extend( perm(pre + str(i), m) )
    return ret

print perm("", range(10))[999999]

