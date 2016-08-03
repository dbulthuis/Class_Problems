#!/usr/bin/python

import sys

oldKey = None
totalsDict = {}
totalForKey = 0

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 3:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisType, thisLength = data_mapped

    if oldKey and oldKey != thisKey:
        output = oldKey + "\t" + str(totalsDict['question']) + "\t"
        if 'answer' not in totalsDict:
            output += "0"
        else :
            output += str(totalsDict['answer']/(totalForKey-1))
        print output
        oldKey = thisKey;
        totalForKey = 0
        totalsDict = {}

    oldKey = thisKey
    if thisType in totalsDict:
        totalsDict[thisType] += float(thisLength)
    else :
        totalsDict[thisType] = float(thisLength)
    totalForKey += 1

if oldKey:
    output = oldKey + "\t" + str(totalsDict['question']) + "\t"
    if 'answer' not in totalsDict:
        output += "0"
    else:
        output += str(totalsDict['answer'] / (totalForKey - 1))
    print output
