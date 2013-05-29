#!/usr/bin/python

seen = {}
seen[1] = 1

def collatz(n):

    if n in seen:
        return seen[n]

    if n % 2:
        nxt = 3 * n + 1
        dist = collatz(nxt) + 1
    else:
        nxt = n / 2
        dist = collatz(nxt) + 1

    seen[n] = dist
    return dist

maxdist = 0
maxval = 0

for i in xrange(1, 1000000):
    dist = collatz(i)
    if dist > maxdist:
        maxdist, maxval = dist, i

print maxval
