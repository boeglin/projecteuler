#!/usr/bin/python

import math

f = open("words.txt").read()
f = f.replace('"', '')
f = f.split(',')

# filter anagrams
def sorta(word):
    return "".join(sorted(list(word)))

grams = {}
for w in f:
    a = sorta(w)
    l = grams.setdefault(a, [])
    l.append(w)

# build square dict
square = {}
for i in xrange(2, 10):
    l = square.setdefault(i, [])
    mini = int(math.ceil(math.sqrt(10 ** (i - 1))))
    maxi = int(math.sqrt((10 ** i) - 1))
    for j in xrange(mini, maxi + 1):
        l.append(j ** 2)


def pair(a, b):
    # test all squares of same length
    return len(a)


maxi = 0
for a in grams:
    l = grams[a]
    if len(l) < 2:
        continue

    m = pair(l[0], l[1])
    if m > maxi:
        maxi = m

    if len(l) == 3:
        m = pair(l[0], l[2])
        if m > maxi:
            maxi = m
        pair(l[1], l[2])
        if m > maxi:
            maxi = m
print maxi

