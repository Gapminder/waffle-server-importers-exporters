from types import *
import xlrd


def read(source, sheet_index, sheet_name):
    book = xlrd.open_workbook(source)
    print 'Reading' + source
    if type(sheet_index) is IntType:
        sh = book.sheet_by_index(sheet_index)
    else:
        sh = book.sheet_by_name(sheet_name)

    return sh
