#!/usr/bin/env python
# -*- coding: utf-8 -*-

import writers.json_local
import util.math
import ws_export.util.name_match
import readers.excel
import util.url
import re
import ws_import.procedures.gw.synonyms
import os.path
from decimal import Decimal


def write_indicators(indicator_url, indicator_id):
    non_decimal = re.compile(r'[^\d.]+')

    indicators_data = []

    entity_names = ws_import.procedures.gw.synonyms.get_entity_synonyms()


    #TODO: make this check the checksum and download if changes happened
    if not os.path.isfile('data/tmp/excel/' + indicator_id + '.xls'):
        util.url.save_remote_spreadsheet(indicator_url, 'data/tmp/excel/' + indicator_id + '.xls')
    data_sheet = readers.excel.read('data/tmp/excel/' + indicator_id + '.xls', None, 'Data')[0]

    non_empty_rows = []
    for rx in range(1, data_sheet.nrows):
        value = data_sheet.cell_value(rowx=rx, colx=0)
        if not value.isspace():
            non_empty_rows.append(rx)

    non_empty_columns = []
    for colx in range(1, data_sheet.ncols):
        value = data_sheet.cell_value(rowx=0, colx=colx)
        try:
            float(value)
            non_empty_columns.append(colx)
        except ValueError:
            print ""



    if len(non_empty_columns) > 0 and len(non_empty_rows) > 0:
    # for rx in range(1, data_sheet.nrows):
    #    for colx in range(1, data_sheet.ncols):
        for rx in range(min(non_empty_rows), max(non_empty_rows) + 1):
            for colx in range(min(non_empty_columns), max(non_empty_columns) + 1):
                value = data_sheet.cell_value(rowx=rx, colx=colx)

                geo = ws_export.util.name_match.set_name_match_val(data_sheet.cell_value(rowx=rx, colx=0), entity_names,
                                                                    13).encode(encoding='UTF-8')

                if type(value) is unicode:
                    try:
                        value = float(value.encode('UTF-8'))
                    except ValueError:
                        continue

                if type(value) is float or type(value) is int:
                #if util.math.empty(value):
                    year = data_sheet.cell_value(rowx=0, colx=colx)

                    if type(year) is unicode:
                        year = year.encode('UTF-8')

                    if type(year) is str:
                       year = float(non_decimal.sub('', year))

                    #geo = ws_export.util.name_match.set_name_match_val(data_sheet.cell_value(rowx=rx, colx=0), entity_names,
                    #                                                   13).encode(encoding='UTF-8')

                    try:
                        float(geo[1:])
                        is_name_matched = True
                    except ValueError:
                        is_name_matched = False

                    if ((type(value) is float) or (type(value) is int)) and is_name_matched:
                        #indicator_value = str('%0.15g' % value)
                        #indicator_value = str('%0.25g' % value)
                        indicator_value = str('%0.4g' % value)


                        data = {'geo': geo,
                                indicator_id: indicator_value,
                                'time': year}
                        indicators_data.append(data)


    writers.json_local.write('data/out/gw/indicators/', indicator_id, indicators_data)


#UNCOMMENT HERE: write_indicators('http://spreadsheets.google.com/pub?key=0ArfEDsV3bBwCdGhSY2trbEVpYnNsMENqendaVm5ucnc', '0ArfEDsV3bBwCdGhSY2trbEVpYnNsMENqendaVm5ucnc')
