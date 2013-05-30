#!/usr/bin/python

def tolist(n):
    while n:
        yield (n % 10) ** 2
        n /= 10

chain = {}
def fchain(n):
    l = []
    nxt = n
    while (nxt != 1 and nxt != 89) and nxt not in chain:
        l.append(nxt)
        nxt = sum(tolist(nxt))

    if nxt == 1 or nxt == 89: # out of cache chain ended
        for i in l:
            chain[i] = nxt
        return nxt == 89 and 1 or 0
    nxt = chain[nxt] # cache hit
    if l: # cache hit after a while
        for i in l:
            chain[i] = nxt
    return nxt == 89 and 1 or 0

acc = 0
for i in xrange(1, 10000000):
    acc += fchain(i)
print acc, len(chain)

