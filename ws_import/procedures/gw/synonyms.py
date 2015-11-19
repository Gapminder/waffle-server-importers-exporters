import readers.excel

#TODO: blend this outside gw modules


def get_entity_synonyms():
    country_synonym_list = readers.excel.read('data/synonym/country_synonyms.xlsx', 0, None)
    country_synonym = country_synonym_list[0]
    entity_names = [[0 for x in range(0, country_synonym.ncols)] for x in range(1, country_synonym.nrows)]

    for r_num in range(1, country_synonym.nrows):
        for c_num in range(0, country_synonym.ncols):
            entity_names[r_num - 1][c_num] = country_synonym.cell_value(rowx=r_num, colx=c_num)

    return entity_names