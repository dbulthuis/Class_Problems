#!/usr/bin/python

import sys

hitsTotal = 0

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 1:
        # Something has gone wrong. Skip this line.
        continue

    request_name, = data_mapped
# '/assets/img/search-button.gif'
#
    if '/assets/js/the-associates.js' in request_name:
        hitsTotal += 1

print hitsTotal

