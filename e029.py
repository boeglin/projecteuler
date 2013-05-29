#!/usr/bin/python

l = []

for a in xrange(2, 101):
    s = a
    for b in xrange(2, 101):
        s = s * a
        if s not in l:
            l.append(s)
print len(l)
