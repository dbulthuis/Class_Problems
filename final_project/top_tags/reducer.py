#!/usr/bin/python

import sys

oldKey = None
topTen = []
totalForKey = 0


def add_top_ten(old_key):
    if len(topTen) < 10:
        topTen.append([totalForKey, old_key])
    else:
        m = min(topTen)
        if m[0] < totalForKey:
            topTen.remove(m)
            topTen.append([totalForKey, old_key])

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisId = data_mapped

    if oldKey and oldKey != thisKey:
        add_top_ten(oldKey)
        oldKey = thisKey;
        totalForKey = 0

    oldKey = thisKey
    totalForKey += 1

if oldKey:
    add_top_ten(oldKey)
    for t in sorted(topTen, reverse=True):
        print t[1],"\t",t[0]
