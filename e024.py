#!/usr/bin/python

def perm(l):
    if not l:
        yield ""

    for i in l:
        m = l[:]
        m.remove(i)
        for j in perm(m):
            yield str(i) + j

count = 0

for i in perm(range(10)):
    count += 1
    if count == 1000000:
        print i
        break

