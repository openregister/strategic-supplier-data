#!/usr/bin/env python3

import sys
import csv

fields = ['strategic-supplier', 'name', 'company', 'crown-representative', 'start-date', 'end-date']
sep = '\t'

#
#  fixup by name
#
names = {}
for row in csv.DictReader(open('fixup/name.tsv'), delimiter=sep):
    names[row['name']] = row


#
#  default missing values
#
def default(row, field):
    return names.get(row['name'], {}).get(field, '')


print(sep.join(fields))

for row in csv.DictReader(sys.stdin, delimiter=sep):

    row['strategic-supplier'] = default(row, 'strategic-supplier')
    row['name'] = default(row, 'name')
    row['company'] = default(row, 'company')
    row['start-date'] = default(row, 'start-date')
    row['end-date'] = default(row, 'end-date')

    if row['crown-representative'] == 'TBC':
        row['crown-representative'] = ''

    print(sep.join([row[field] for field in fields]))
