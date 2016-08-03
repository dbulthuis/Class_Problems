#!/usr/bin/python

import sys

oldKey = None
studentList = []

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisStudent = data_mapped

    if oldKey and oldKey != thisKey:
        print oldKey,'\t',studentList
        oldKey = thisKey;
        studentList = []

    oldKey = thisKey
    studentList.append(int(thisStudent))

if oldKey:
    print oldKey, '\t', studentList
