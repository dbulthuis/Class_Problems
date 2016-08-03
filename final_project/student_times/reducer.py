#!/usr/bin/python

import sys

oldKey = None
hoursDict = {}

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisHour = data_mapped

    if oldKey and oldKey != thisKey:
        maxHours = max(hoursDict.values())
        for x in sorted(zip(hoursDict.values(),hoursDict.keys())) :
            if x[0] == maxHours :
                print oldKey, "\t", x[1]
        oldKey = thisKey;
        hoursDict = {}

    oldKey = thisKey
    if thisHour in hoursDict:
        hoursDict[thisHour] += 1
    else :
        hoursDict[thisHour] = 1

if oldKey:
    maxHours = max(hoursDict.values())
    for x in sorted(zip(hoursDict.values(), hoursDict.keys())):
        if x[0] == maxHours:
            print oldKey, "\t", x[1]
