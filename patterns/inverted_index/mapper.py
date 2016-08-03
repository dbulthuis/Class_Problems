#!/usr/bin/python

# Format of each line is:
# "id"	"title"	"tagnames"	"author_id"	"body"	"node_type"	"parent_id"	"abs_parent_id"	"added_at"	"score"	
# "state_string"	"last_edited_id"	"last_activity_by_id"	"last_activity_at"	"active_revision_id"	
# "extra"	"extra_ref_id"	"extra_count"	"marked"

import sys
import re
import csv

reader = csv.reader(sys.stdin, delimiter='\t')

for data in reader:
    if len(data) >= 5:
        body_words = re.split('\W+', data[4])
        for word in body_words:
            if len(word) > 5:
                print "{0}\t{1}".format(word.lower().capitalize(), data[0])