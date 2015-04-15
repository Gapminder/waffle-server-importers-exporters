def set_name_match_val(country, entity_names):
    for row in range(0, len(entity_names)):
            for column in range(0, len(entity_names[0])):
                if country == entity_names[row][column]:
                    country = entity_names[row][13]
                    return country

    return country