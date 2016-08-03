#!/usr/bin/python

import sys
import pprint

node_set = []
oldWord = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisWord, thisId = data_mapped

    if oldWord and oldWord != thisWord:
        #print oldWord, "\t", sorted(node_set)
        print oldWord, "\t", len(node_set)
        oldWord = thisWord;
        node_set = []

    oldWord = thisWord
    node_set.append(thisId)

if oldWord:
    print oldWord, "\t", len(node_set)

