#!/usr/bin/env python3

#
#  extract table from .docx as TSV
#

import sys
from docx.api import Document

document = Document(sys.argv[1])
table = document.tables[0]

fields = ()
sep = '\t'

def list_strip(_list):
    return [e.strip() for e in _list]

for i, row in enumerate(table.rows):
    text = (cell.text for cell in row.cells)

    if i == 0:
        fields = list_strip(text)
        print(sep.join(fields))
        continue

    row = dict(zip(fields, list_strip(text)))

    print(sep.join([row[field] for field in fields]))
