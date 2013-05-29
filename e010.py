#!/usr/bin/python

import math

N = 2000000

mult = [0] * N

msum = 2 # start at three

for i in xrange(3, N, 2):
    if mult[i]:
        continue

    for j in xrange(3, int(math.sqrt(i)) + 1, 2):
        if not i % j:
            break;
    else:
        msum += i
        acc = 2 * i
        while acc < N:
            mult[acc] = 1;
            acc += i

print msum

