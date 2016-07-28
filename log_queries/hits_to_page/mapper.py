#!/usr/bin/python

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment
#
# We want elements 2 (item name) and 4 (cost)
# We need to write them out to standard output, separated by a tab
# %h is the IP address of the client
# %l is identity of the client, or "-" if it's unavailable
# %u is username of the client, or "-" if it's unavailable
# %t is the time that the server finished processing the request. The format is [day/month/year:hour:minute:second zone]
# %r is the request line from the client is given (in double quotes). It contains the method, path, query-string, and protocol or the request.
# %>s is the status code that the server sends back to the client. You will see see mostly status codes 200 (OK - The request has succeeded), 304 (Not Modified) and 404 (Not Found). See more information on status codes in W3C.org
# %b is the size of the object returned to the client, in bytes. It will be "-" in case of status code 304.

import sys
import re

regex = re.compile('([^ ]*) ([^ ]*) ([^ ]*) \[([^]]*)\] "([^"]*)" ([^ ]*) ([^ ]*)' )

for line in sys.stdin:
    data = regex.match(line)

    if data and len(data.groups()) == 7:
        ip, identity, username, finish_time, request_line, status_code, size = data.groups()
        print "{0}".format(request_line)

