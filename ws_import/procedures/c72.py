def cal_name_match(country_synonym, merged_pop):
    entity_names = [[0 for x in range(0, country_synonym.ncols)] for x in range(1, country_synonym.nrows)]

    for r_num in range(1, country_synonym.nrows):
        for c_num in range(0, country_synonym.ncols):
            entity_names[r_num - 1][c_num] = country_synonym.cell_value(rowx=r_num, colx=c_num)

    print "Name-matching the merged population values"
    for element in merged_pop:
        element = set_name_match_val(element, entity_names)

    return merged_pop


def set_name_match_val(element, entity_names):
    for row in range(0, len(entity_names)):
            for column in range(0, len(entity_names[0])):
                if element['Area'] == entity_names[row][column]:
                    element['Area'] = entity_names[row][8]
                    return element

    return element