from typing import List
from stock import Stock


class TableFormatter:
    def headings(self, headers):
        '''Emit table headings.'''
        raise NotImplementedError()

    def row(serf, rowdata):
        '''Emit a single row of table data.'''
        raise NotImplementedError()


class TextTableFormatter(TableFormatter):
    '''Emit a table in plain-text format.'''
    def headings(self, headers):
        for h in headers:
            print(f'{h:>10s}', end=' ')
        print()
        print(('-' * 10 + ' ') * len(headers))
    
    def row(self, rowdata):
        for d in rowdata:
            print(f'{d:>10s}', end=' ')
        print()


class CSVTableFormatter(TableFormatter):
    '''Output portfolio data in CSV format.'''
    def headings(self, headers):
        print(','.join(headers))

    def row(self, rowdata):
        print(','.join(rowdata))


class HTMLTableFormatter(TableFormatter):
    '''Output portfolio data as HTML table.'''
    def headings(self, headers):
        print('<tr>', end='')
        for h in headers:
            print(f'<th>{h}</th>', end='')
        print('</tr>')
    
    def row(self, rowdata):
        print('<tr>', end='')
        for d in rowdata:
            print(f'<td>{d}</td>', end='')
        print('</tr>')


def create_formatter(name):
    if name == 'txt':
        return TextTableFormatter()
    elif name == 'csv':
        return CSVTableFormatter()
    elif name == 'html':
        return HTMLTableFormatter()
    else:
        raise RuntimeError(f'Unknown format {name}')


def print_table(data: List[Stock], columns: List[str], formatter: str):
    formatter.headings(columns)
    for obj in data:
        rowdata = [str(getattr(obj, colname)) for colname in columns]
        formatter.row(rowdata)
