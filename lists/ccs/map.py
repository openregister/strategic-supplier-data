#!/usr/bin/env python3

import sys
import csv

sep = '\t'
fields = ['name', 'crown-representative']

print(sep.join(fields))

for row in csv.DictReader(sys.stdin, delimiter=sep):

    row['name'] = row['Strategic Supplier']
    row['crown-representative'] = row['Crown Representative']

    print(sep.join([row[field] for field in fields]))
