#!/usr/bin/python

# Format of each line is:
# "id"	"title"	"tagnames"	"author_id"	"body"	"node_type"	"parent_id"	"abs_parent_id"	"added_at"	"score"	
# "state_string"	"last_edited_id"	"last_activity_by_id"	"last_activity_at"	"active_revision_id"	
# "extra"	"extra_ref_id"	"extra_count"	"marked"

import sys
import csv
from datetime import datetime

reader = csv.reader(sys.stdin, delimiter='\t')

for data in reader:
    if len(data) >= 9:
        if data[5] == 'answer':
            print "{0}\t{1}\t{2}".format(data[6], data[5], len(data[4]))
        else :
            print "{0}\t{1}\t{2}".format(data[0], data[5], len(data[4]))
