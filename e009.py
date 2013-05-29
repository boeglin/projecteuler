#!/usr/bin/python

def triplet(n):
    for a in xrange(n / 3):
        for b in xrange(a + 1, (n - (a + 1)) / 2 + 1):
            c = n - a - b
            if a ** 2 + b ** 2 == c ** 2:
                return a * b * c

print triplet(1000)

