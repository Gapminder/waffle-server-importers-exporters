import readers.excel
import readers.json_reader

import procedures.c72
import procedures.c73
import procedures.c74
import procedures.c75
import procedures.c78
import procedures.c79

import writers.json_local

pop_list = readers.excel.read('../data/stats/excel/pop_dev.xlsx', None, 'Data')

#TODO: refactor reader's class to set versions there
#sh_meta = readers.excel.read('../data/stats/excel/pop_dev.xlsx', None, 'Information')
#pop_version = sh_meta.cell_value(rowx=6, colx=2)
pop_version = 3.0

pop = procedures.c73.cal_pop_country_values(pop_list, pop_version)
world_pop = procedures.c74.cal_world_pop(pop, pop_version)

entities_geo = readers.json_reader.read('../data/entities/entities-geo.json')
regions_pop = procedures.c75.cal_pop_for_regions(pop, entities_geo, pop_version)

merged_pop = procedures.c78.calc_merge_pop(regions_pop, world_pop, pop)

country_synonym_list = readers.excel.read('../data/synonym/country_synonyms.xlsx', 0, None)
name_matched_merged_pop = procedures.c72.cal_name_match(country_synonym_list, merged_pop)

final_pop = procedures.c79.map_keys_pop(name_matched_merged_pop)

writers.json_local.write('pop', final_pop)















