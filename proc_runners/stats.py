import time
import pop
import lex
import gdp
import procedures.merge

import readers.json_reader
import writers.json_remote


url = 'https://waffle-server-amir.herokuapp.com/waffles/import'
time_now = time.gmtime()

version = str(time_now.tm_year) + '-' + str(time_now.tm_mon) + '-' + str(time_now.tm_mday) + 'T' + str(time_now.tm_hour) + ':' + str(time_now.tm_min) + ':' + str(time_now.tm_sec) + "Z"


def push_stats():
    results = procedures.merge.merge(pop.cal_pop() + lex.cal_lex() + gdp.cal_gdp())
    writers.json_remote.write(url, results, 'stats', version)


def push_entities():
    results = readers.json_reader.read('../data/entities/entities-geo.json')
    writers.json_remote.write(url, results, 'entities', version)


def push_dimensions():
    results = readers.json_reader.read('../data/dimensions/dimensions.json')
    writers.json_remote.write(url, results, 'dimensions', version)


def push_quantities():
    results = readers.json_reader.read('../data/quantities/quantities.json')
    writers.json_remote.write(url, results, 'quantities', version)
