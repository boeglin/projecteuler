#!/usr/bin/python

acc = 0
for i in xrange(2, 200000):
    l = [int(x) ** 5 for x in list(str(i))]
    msum = reduce(lambda x, y: x + y, l)
    if msum == i:
        print i
        acc += i
print acc
