#!/usr/bin/python

import math

count = 1 # because the while loop starts at 3
i = 1

while count < 10001:
    i += 2
    for j in xrange(3, int(math.sqrt(i)) + 1, 2):
        if not i % j:
            break;
    else:
        count += 1

print i

