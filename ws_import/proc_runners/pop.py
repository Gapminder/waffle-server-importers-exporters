import readers.excel
import readers.json_reader

import ws_import.procedures.c72
import ws_import.procedures.c73
import ws_import.procedures.c74
import ws_import.procedures.c75
import ws_import.procedures.c78
import ws_import.procedures.c79


def cal_pop():

    read = readers.excel.read('data/stats/excel/pop_dev.xlsx', None, 'Data')
    pop_list = read[0]
    read_map = read[1]

    pop_version = 3.0
    col_val = 3
    filter_columns = ['Population', 'Population with interpolations', 'Year', 'Area', 'Source']
    read_columns = {c_key: read_map[c_key] for c_key in filter_columns}

    column_mapping = dict(read_columns.items())

    pop = ws_import.procedures.c73.cal_pop_country_values(pop_list, column_mapping, col_val)
    world_pop = ws_import.procedures.c74.cal_world_pop(pop, column_mapping, col_val)

    entities_geo = readers.json_reader.read('data/out/waffle/entities/entities-geo.json')
    regions_pop = ws_import.procedures.c75.cal_pop_for_regions(pop, entities_geo, column_mapping, col_val)

    merged_pop = ws_import.procedures.c78.calc_merge_pop(regions_pop, world_pop, pop)

    country_synonym_list = readers.excel.read('data/synonym/country_synonyms.xlsx', 0, None)
    name_matched_merged_pop = ws_import.procedures.c72.cal_name_match(country_synonym_list[0], merged_pop)

    map_keys = {'Area': 'geo', 'Year': 'time', 'Population with interpolations': 'pop'}
    final_pop = ws_import.procedures.c79.map_keys_pop(name_matched_merged_pop, map_keys)

    return final_pop

















