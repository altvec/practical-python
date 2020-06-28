# fileparse.py
#
# Exercise 3.3

import csv


def parse_csv(
    lines,
    select=None,
    types=None,
    has_headers=True,
    delimiter=',',
    silence_errors=False,
    ):
    '''
    Parse a CSV file into a list of records.
    '''
    if select and not has_headers:
        raise RuntimeError("Select argument requires column headers")

    rows = csv.reader(lines, delimiter=delimiter)
    headers = next(rows) if has_headers else []
    if select:
        indices = [headers.index(colname) for colname in select]
        headers = select
    records = []
    for idx, row in enumerate(rows, start=1):
        if not row:
            continue
        if select:
            row = [row[index] for index in indices]
        if types:
            try:
                row = [func(val) for func, val in zip(types, row)]
            except ValueError as e:
                if not silence_errors:
                    print(f'Row {idx}: Couldn\'t convert {row}')
                    print(f'Row {idx}: Reason {e}')
                continue
        if headers:
            record = dict(zip(headers, row))
        else:
            record = tuple(row)
        records.append(record)
    return records