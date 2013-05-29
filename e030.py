#!/usr/bin/python

acc = 0
for i in xrange(2, 200000):
    msum = sum((int(x) ** 5 for x in list(str(i))))
    if msum == i:
        acc += i
print acc

