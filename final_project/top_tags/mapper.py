#!/usr/bin/python

# Format of each line is:
# "id"	"title"	"tagnames"	"author_id"	"body"	"node_type"	"parent_id"	"abs_parent_id"	"added_at"	"score"	
# "state_string"	"last_edited_id"	"last_activity_by_id"	"last_activity_at"	"active_revision_id"	
# "extra"	"extra_ref_id"	"extra_count"	"marked"

import sys
import csv
import re

reader = csv.reader(sys.stdin, delimiter='\t')

for data in reader:
    if len(data) >= 9:
        tags = re.split('\W+', data[2])
        for tag in set(tags):
            print "{0}\t{1}".format(tag, data[0])
