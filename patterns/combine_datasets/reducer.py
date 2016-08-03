#!/usr/bin/python
# Here you will be able to combine the values that come from 2 sources
# Value that starts with A will be the user data
# Values that start with B will be forum node data

import csv
import sys

def reducer():
    reader = csv.reader(sys.stdin, dialect='excel', delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

    user_ptr_id = "u"
    author_id = "a"

    for line in reader:

        if len(line) == 6:
            user_ptr_id, lit_A, reputation, gold, silver, bronze = line

        if len(line) == 11:
            author, lit_B, nodeid, title, author_id, tagnames, node_type, parent_id, abs_parent_id, added_at, score = line

        if user_ptr_id == author_id:
            line = [nodeid, lit_B, title, tagnames, author_id, node_type, parent_id, abs_parent_id, added_at,score,
                    reputation, gold, silver, bronze]
            writer.writerow(line)

reducer()