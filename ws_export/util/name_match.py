import readers.json_reader

# TODO: make it higher level, import is using it
def set_name_match_val(country, entity_names, dest_column):
    for row in range(0, len(entity_names)):
            for column in range(0, len(entity_names[0])):
                if country == entity_names[row][column]:
                    country = entity_names[row][dest_column]
                    return country

    return country


def set_name_match_val_region(region_name):
    regions_synonym = readers.json_reader.read('../../data/synonym/regions.json')
    for region in regions_synonym:
        if region_name in region:
            return region[region_name]
    return region_name