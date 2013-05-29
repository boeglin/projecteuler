#!/usr/bin/python

f = open("names.txt").read()
f = f.replace('"', '')
f = f.split(',')
f.sort()

i = 0
acc = 0
for n in f:
    i += 1
    nv = 0
    for l in n:
        nv += ord(l) - ord('A') + 1
    acc += i * nv

print acc

