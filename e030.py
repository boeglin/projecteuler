#!/usr/bin/python

def tolist(n):
    while n:
        yield (n % 10) ** 5
        n /= 10

acc = 0
for i in xrange(2, 200000):
    msum = sum(tolist(i))
    if msum == i:
        acc += i
print acc

