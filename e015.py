#!/usr/bin/python

N = 20
found = {}

def choose(r, d, pre = ''):
    ret = 0

    if not (r or d):
        return 1

    if pre in found:
        return found[pre]

    if r:
        ret += choose(r - 1, d, pre + 'r')
    if d:
        ret += choose(r, d - 1, 'd' + pre)

    found[pre] = ret
    return ret

print choose(N, N)

