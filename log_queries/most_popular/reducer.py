#!/usr/bin/python

import sys

timesAppeared = 0
oldKey = None
mostPopular = None
mostPopularTimesAppeared = 0

# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the sale amount
#
# All the sales for a particular store will be presented,
# then the key will change and we'll be dealing with the next store

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 1:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, = data_mapped

    if oldKey and oldKey != thisKey:
        if timesAppeared > mostPopularTimesAppeared :
            mostPopularTimesAppeared = timesAppeared
            mostPopular = oldKey
        #print oldKey, "\t", timesAppeared
        oldKey = thisKey
        timesAppeared = 0

    oldKey = thisKey
    timesAppeared += 1

if oldKey:
    #print oldKey, "\t", timesAppeared
    if timesAppeared > mostPopularTimesAppeared:
        mostPopularTimesAppeared = timesAppeared
        mostPopular = oldKey
    print mostPopular, "\t", mostPopularTimesAppeared
