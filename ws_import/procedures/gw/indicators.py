import writers.json_local
import util.math
import ws_export.util
import readers.excel
import util.url
import ws_import.procedures.gw.synonyms
import util.log


def write_indicators(indicator_url, indicator_id):

    util.log.set_info('INFO: reading indicator file: ' + indicator_id + '...')
    indicators_data = []
    entity_names = ws_import.procedures.gw.synonyms.get_entity_synonyms()

    util.url.save_remote_spreadsheet(indicator_url, '../../data/tmp/excel/' + indicator_id + '.xls')

    data_sheet = readers.excel.read('../../data/tmp/excel/' + indicator_id + '.xls', None, 'Data')[0]

    for rx in range(1, data_sheet.nrows):
        for colx in range(1, data_sheet.ncols):
            if util.math.empty(data_sheet.cell_value(rowx=rx, colx=colx)):
                geo = ws_export.util.name_match.set_name_match_val(data_sheet.cell_value(rowx=rx, colx=0), entity_names,
                                                                   13).decode(encoding='UTF-8')
                data = {'geo': geo,
                        indicator_id: data_sheet.cell_value(rowx=rx, colx=colx),
                        'time': data_sheet.cell_value(rowx=0, colx=colx)}
                indicators_data.append(data)

    writers.json_local.write('../../data/out/gw/indicators/', indicator_id, indicators_data)
    util.log.set_info('pushed ' + indicator_id + '...')

