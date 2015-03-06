import readers.excel
import readers.json_reader

import procedures.c72
import procedures.c73
import procedures.c74
import procedures.c75
import procedures.c78
import procedures.c79


def cal_gdp():

    read = readers.excel.read('../data/stats/excel/gdp_dev.xlsx', None, 'Data & metadata')
    lex_list = read[0]
    read_map = read[1]

    gdp_version = 14.0
    col_val = 2
    filter_columns = ['GDP per capita - with interpolations', 'Year', 'Area', 'Source']
    read_columns = {c_key: read_map[c_key] for c_key in filter_columns}
    const = {'dim': 'geo-time', 'version': str(gdp_version)}

    column_mapping = dict(read_columns.items() + const.items())

    gdp = procedures.c73.cal_pop_country_values(lex_list, column_mapping, col_val)
    world_gdp = procedures.c74.cal_world_pop(gdp, column_mapping, col_val)

    entities_geo = readers.json_reader.read('../data/entities/entities-geo.json')
    regions_gdp = procedures.c75.cal_pop_for_regions(gdp, entities_geo, column_mapping, col_val)

    merged_gdp = procedures.c78.calc_merge_pop(regions_gdp, world_gdp, gdp)

    country_synonym_list = readers.excel.read('../data/synonym/country_synonyms.xlsx', 0, None)
    name_matched_merged_gdp = procedures.c72.cal_name_match(country_synonym_list[0], merged_gdp)

    map_keys = {'Area': 'geo', 'Year': 'time', 'GDP per capita - with interpolations': 'gdp'}
    final_gdp = procedures.c79.map_keys_pop(name_matched_merged_gdp, map_keys)

    return final_gdp


