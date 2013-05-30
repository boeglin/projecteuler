#!/usr/bin/python

import math

f = open("words.txt").read()
f = f.replace('"', '')
f = f.split(',')

# unique key
def sorta(word):
    return "".join(sorted(list(word)))

# build lists of anagrams
grams = {}
for w in f:
    a = sorta(w)
    l = grams.setdefault(a, [])
    l.append(w)

# build squares dict
squares = {}
for i in xrange(2, 10):
    l = squares.setdefault(i, [])
    mini = int(math.ceil(math.sqrt(10 ** (i - 1))))
    maxi = int(math.sqrt((10 ** i) - 1))
    for j in xrange(mini, maxi + 1):
        l.append(str(j ** 2))

# test pair of words
def pair(a, b):
    ret = [0]
    # test all squares of same length
    sq = squares[len(a)]
    for s in sq:
        dup = []
        tr = {}
        for x in xrange(len(a)):
            tr[a[x]] = s[x]
            if s[x] not in dup:
                dup.append(s[x])
            else:
                # multiple letters have the same value
                break;
        else:
            nb = ''
            for x in b:
                nb += tr[x]
            if nb in sq:
                ret.append(int(nb))

    return max(ret)

# test anagram pairs
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

