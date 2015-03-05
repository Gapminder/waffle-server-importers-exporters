import readers.excel
import readers.json_reader

import procedures.c72
import procedures.c73
import procedures.c74
import procedures.c75
import procedures.c78
import procedures.c79

import writers.json_local
import writers.json_remote

read = readers.excel.read('../data/stats/excel/pop_dev.xlsx', None, 'Data')
pop_list = read[0]
read_map = read[1]

pop_version = 3.0
col_val = 3
filter_columns = ['Population', 'Population with interpolations', 'Year', 'Area']
read_columns = {c_key: read_map[c_key] for c_key in filter_columns}
const = {'dim': 'geo-time', 'version': str(pop_version), 'Source': 'No Data'}

column_mapping = dict(read_columns.items() + const.items())

pop = procedures.c73.cal_pop_country_values(pop_list, column_mapping, col_val)
world_pop = procedures.c74.cal_world_pop(pop, column_mapping, col_val)

entities_geo = readers.json_reader.read('../data/entities/entities-geo.json')
regions_pop = procedures.c75.cal_pop_for_regions(pop, entities_geo, column_mapping, col_val)

merged_pop = procedures.c78.calc_merge_pop(regions_pop, world_pop, pop)

country_synonym_list = readers.excel.read('../data/synonym/country_synonyms.xlsx', 0, None)
name_matched_merged_pop = procedures.c72.cal_name_match(country_synonym_list[0], merged_pop)

final_pop = procedures.c79.map_keys_pop(name_matched_merged_pop)

writers.json_remote.write('https://waffle-server-amir.herokuapp.com/waffles/import', final_pop)















