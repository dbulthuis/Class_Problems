#!/usr/bin/python

# Format of each line is:
# "id"	"title"	"tagnames"	"author_id"	"body"	"node_type"	"parent_id"	"abs_parent_id"	"added_at"	"score"	
# "state_string"	"last_edited_id"	"last_activity_by_id"	"last_activity_at"	"active_revision_id"	
# "extra"	"extra_ref_id"	"extra_count"	"marked"

import sys
import re
import csv
from datetime import datetime

reader = csv.reader(sys.stdin, delimiter='\t')

for data in reader:
    if len(data) >= 9:
        author_id = data[3]
        added_date = datetime.strptime(data[8], "%Y-%m-%d %H:%M:%S.%f+00")
        hour_added = added_date.strftime("%H")
        print "{0}\t{1}".format(author_id, hour_added)