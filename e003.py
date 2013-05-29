#!/usr/bin/python

import math

def primes(n, start=2):
    for i in xrange(start, int(math.sqrt(n)) + 1):
        if not n % i:
            return [i] + primes(n / i, i)
    return [n]

print primes(600851475143)

