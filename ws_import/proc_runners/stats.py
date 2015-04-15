import time

from ws_import.proc_runners import pop
import lex
import gdp
import ws_import.procedures.merge
import readers.json_reader
import writers.json_remote
import writers.json_local


url = 'https://waffle-server-amir.herokuapp.com/waffles/import'
time_now = time.gmtime()

version = str(time_now.tm_year) + '-' + str(time_now.tm_mon) + '-' + str(time_now.tm_mday) + 'T' + \
          str(time_now.tm_hour) + ':' + str(time_now.tm_min) + ':' + str(time_now.tm_sec) + "Z"


def push_stats():
    results = ws_import.procedures.merge.merge(pop.cal_pop() + lex.cal_lex() + gdp.cal_gdp())
    # writers.json_remote.write(url, results, 'stats/geo_time', version)
    writers.json_local.write('stats', results)


def push_entities():
    results = readers.json_reader.read('../data/out/waffle/entities/entities-geo.json')
    # writers.json_remote.write(url, results, 'entities/geo', version)
    writers.json_local.write('entities', results)


def push_dimensions():
    results = readers.json_reader.read('../data/out/waffle/dimensions/dimensions.json')
    # writers.json_remote.write(url, results, 'dimensions', version)
    writers.json_local.write('dimensions', results)


def push_quantities():
    results = readers.json_reader.read('../data/quantities/quantities.json')
    # writers.json_remote.write(url, results, 'quantities', version)
    writers.json_local.write('quantities', results)