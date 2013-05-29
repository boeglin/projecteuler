#!/usr/bin/python

acc = 0

for i in xrange(1000):
    if not (i % 3 and i % 5):
        acc += i

print acc
