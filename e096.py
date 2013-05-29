#!/usr/bin/python

#### those 2 functions brute force the grid 

def is_valid(s):
    #lines
    for y in xrange(9):
        l = []
        for x in xrange(9):
            c = s[y][x]
            if len(c) == 1 and c[0] in l:
                return False
            l.append(c[0])
    # columns
    for x in xrange(9):
        l = []
        for y in xrange(9):
            c = s[y][x]
            if len(c) == 1 and c[0] in l:
                return False
            l.append(c[0])
    # squares
    for y in xrange(0, 9, 3):
        for x in xrange(0, 9, 3):
            l = []
            for j in xrange(y, y + 3):
                for i in xrange(x, x + 3):
                    c = s[j][i]
                    if len(c) == 1 and c[0] in l:
                        return False
                    l.append(c[0])
    return True

def solve(s):
    for y in xrange(9):
        for x in xrange(9):
            if len(s[y][x]) > 1:
                for i in s[y][x]:
                    new_s = [[[c for c in a] for a in b] for b in s]
                    new_s[y][x] = [i]
                    if is_valid(new_s):
                        new_s = solve(new_s)
                        if new_s:
                            return new_s
                return None
    return s

#### those 3 functions cut branches

def clean(cand, x, y, val):
    rem = 0
    # line
    for i in xrange(9):
        if i != x and val in cand[y][i]:
            cand[y][i].remove(val)
            rem += 1
    # column
    for j in xrange(9):
        if j != y and val in cand[j][x]:
            cand[j][x].remove(val)
            rem += 1
    # square
    for j in xrange(y / 3 * 3, y / 3 * 3 + 3):
        for i in xrange(x / 3 * 3, x / 3 * 3 + 3):
            if (i != x or j != y) and val in cand[j][i]:
                cand[j][i].remove(val)
                rem += 1
    return rem

def autoclean(cand):
    ret = 0
    rem = 1 # trick to enter the loop
    while rem > 0:
        rem = 0
        for y in xrange(9):
            for x in xrange(9):
                if len(cand[y][x]) == 1:
                    rem += clean(cand, x, y, cand[y][x][0])
        ret += rem
    return ret

def autofind(cand):
    for y in xrange(9):
        for x in xrange(9):
            if len(cand[y][x]) > 1:
                # line
                other = []
                for i in xrange(9):
                    if i != x:
                        for val in cand[y][i]:
                            if val not in other:
                                other.append(val)
                # test
                if len(other) == 8:
                    for mval in cand[y][x]:
                        if mval not in other:
                            cand[y][x] = [mval]
                            return 1
                # column
                other = []
                for j in xrange(9):
                    if j != y:
                        for val in cand[j][x]:
                            if val not in other:
                                other.append(val)
                # test
                if len(other) == 8:
                    for mval in cand[y][x]:
                        if mval not in other:
                            cand[y][x] = [mval]
                            return 1
                # square
                other = []
                for j in xrange(y / 3 * 3, y / 3 * 3 + 3):
                    for i in xrange(x / 3 * 3, x / 3 * 3 + 3):
                        if i != x or j != y:
                            for val in cand[j][i]:
                                if val not in other:
                                    other.append(val)
                # test
                if len(other) == 8:
                    for mval in cand[y][x]:
                        if mval not in other:
                            cand[y][x] = [mval]
                            return 1
    return 0

#### utilities

def init(s):
    cand = [[[] for _ in xrange(9)] for _ in xrange(9)]
    for y in xrange(9):
        for x in xrange(9):
            if s[y][x]:
                cand[y][x].append(s[y][x])
            else:
                cand[y][x] = range(1, 10)
    return cand

def is_solved(cand):
    for y in xrange(9):
        for x in xrange(9):
            if len(cand[y][x]) != 1:
                return False
    return True

def show(cand):
    for line in cand:
        for item in line:
            for choice in item:
                print choice,
            print ' ' * (12 - len(item) * 2), '|',
        print

#### start

acc = 0
f = open("sudoku.txt").readlines()
for i in xrange(50):
    s = f[10 * i + 1:10 * (i + 1)]
    s = [[int(y) for y in list(x.strip())] for x in s]

    cand = init(s)
    act = 1 # trick to enter the loop
    while act > 0:
        act = 0
        act += autoclean(cand)
        act += autofind(cand)

    if not is_solved(cand):
        print "bruteforce", i
        cand = solve(cand)

    num = int(''.join([str(x[0]) for x in cand[0][:3]]))
    acc += num

print acc

