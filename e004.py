#!/usr/bin/python

def palyn(n):
    return str(n) == str(n)[::-1]

res = 0
N = 999

for i in xrange(N, 0, -1):
    for j in xrange(N, i - 1, -1):
        prod = i * j
        if palyn(prod) and prod > res:
            res = prod

print res

