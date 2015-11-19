import sys
import util.const
import readers.excel

import writers.json_remote
import writers.json_local

import util.math
import util.url
import util.util
import util.log
import util.config

import ws_import.procedures.gw.synonyms
import ws_import.procedures.gw.area_categorization
import ws_import.procedures.gw.indicator_categorization
import ws_import.procedures.gw.indicators
import ws_import.procedures.gw.dimension
import ws_import.procedures.gw.quantities
import time

reload(sys)
sys.setdefaultencoding('utf-8')

url = util.config.get_value('URL', 'waffle')
graph_settings = util.config.get_value('URL', 'graph_settings')
version = util.util.set_timestamp()

#util.url.save_remote_spreadsheet(graph_settings, 'data/meta/graph_settings.xlsx')

# TODO: Only if the checksum is different! or put it in data/tmp folder
about = readers.excel.read('data/meta/graph_settings.xlsx', None, 'About')[0]
indicators = readers.excel.read('data/meta/graph_settings.xlsx', None, 'Indicators')[0]

print 'area categorization:' + str(time.gmtime())
area_categorization = ws_import.procedures.gw.area_categorization.get(about)
writers.json_local.write('data/out/gw/meta/', 'area_categorizarion', area_categorization)
writers.json_remote.write(url, area_categorization, 'meta/area_categorizarion', version)
util.log.set_info('meta/area_categorizarion is pushed')

print 'indicator categorization:' + str(time.gmtime())
#TODO: remove the passing-in function from the procedure
indicator_categorization = ws_import.procedures.gw.indicator_categorization.get(ws_import.procedures.gw.indicators.write_indicators)
writers.json_local.write('data/out/gw/meta/', 'indicator_categorizarion', indicator_categorization)
writers.json_remote.write(url, indicator_categorization, 'meta/indcator_categorizarion', version)
url.log.set_info('meta/indicator_categorizarion is pushed')

print 'dimension:' + str(time.gmtime())
dim = ws_import.procedures.gw.dimension.get(indicators)
writers.json_local.write('data/out/gw/meta/', 'dimensions', dim)
writers.json_remote.write(url, dim, 'dimensions', '2015-4-21T8:9:35Z')
util.log.set_info('meta/dimensions is pushed')


print 'quantities' + str(time.gmtime())
quantities = ws_import.procedures.gw.quantities.get(indicators)
writers.json_local.write('data/out/gw/meta/', 'quantities', quantities)
writers.json_remote.write(url, quantities, 'quantities', '2015-4-21T8:9:35Z')
util.log.set_info('meta/quantities is pushed')

print 'Import From Spreadsheets is Finished'













