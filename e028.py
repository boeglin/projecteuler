#!/usr/bin/python


nxt = 3
count = 0
bloc = 2

acc = 0
for i in xrange(3, 1001 * 1001 + 1, 2):
    if i < nxt:
        continue
    else:
        acc += i

        count += 1
        if count > 3:
            count = 0
            bloc += 2

        nxt += bloc

print acc + 1

