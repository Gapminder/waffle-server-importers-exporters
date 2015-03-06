import readers.excel
import readers.json_reader

import procedures.c72
import procedures.c73
import procedures.c74
import procedures.c75
import procedures.c78
import procedures.c79

def cal_lex():
    read = readers.excel.read('../data/stats/excel/lex_dev.xlsx', None, 'Data & metadata')
    lex_list = read[0]
    read_map = read[1]

    lex_version = 6.0
    col_val = 3
    filter_columns = ['Life expectancy at birth - with interpolations', 'Year', 'Area', 'Source']
    read_columns = {c_key: read_map[c_key] for c_key in filter_columns}
    const = {'dim': 'geo-time', 'version': str(lex_version)}

    column_mapping = dict(read_columns.items() + const.items())

    lex = procedures.c73.cal_pop_country_values(lex_list, column_mapping, col_val)
    world_lex = procedures.c74.cal_world_pop(lex, column_mapping, col_val)

    entities_geo = readers.json_reader.read('../data/entities/entities-geo.json')
    regions_lex = procedures.c75.cal_pop_for_regions(lex, entities_geo, column_mapping, col_val)

    merged_lex = procedures.c78.calc_merge_pop(regions_lex, world_lex, lex)

    country_synonym_list = readers.excel.read('../data/synonym/country_synonyms.xlsx', 0, None)
    name_matched_merged_lex = procedures.c72.cal_name_match(country_synonym_list[0], merged_lex)

    map_keys = {'Area': 'geo', 'Year': 'time', 'Life expectancy at birth - with interpolations': 'lex'}
    final_lex = procedures.c79.map_keys_pop(name_matched_merged_lex, map_keys)

    return final_lex















