#!/usr/bin/python

acc = 0
for i in xrange(1, 1000001):
    s = str(i)
    b = bin(i)[2:]
    if s == s[::-1] and b == b[::-1]:
        acc += i
        print acc, i
