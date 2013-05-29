#!/usr/bin/python

tri = open("triangle.txt").read()
tri = tri.strip().split('\n')

tri = [x.split() for x in tri]

dep = len(tri) - 1

path = {}
for i in xrange(dep):
    path[i] = {}

def trip(x = 0, y = 0):
    if x == dep:
        return int(tri[x][y])

    if y in path[x]:
        return path[x][y]

    a = trip(x + 1, y)
    b = trip(x + 1, y + 1)
    ret = max(a, b) + int(tri[x][y])
    path[x][y] = ret
    return ret

print trip()

