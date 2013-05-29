#!/usr/bin/python

N = 100

a = sum((x ** 2 for x in xrange(1, N + 1)))

b = sum(xrange(1, N + 1)) ** 2

print b - a

