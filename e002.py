#!/usr/bin/python

acc = 0

a = 1
b = 1
while b < 4e6:
    if not b % 2:
        acc += b
    a = a + b
    a, b = b, a

print acc

