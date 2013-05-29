#!/usr/bin/python

N = 20

res = 1
for x in xrange(2, N + 1):
    if res % x:
        for y in xrange(2, N + 1):
            if not res * y % x:
                res *= y
                break

print res

