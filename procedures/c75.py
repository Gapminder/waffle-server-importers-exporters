def get_region_names(entities_geo, region_id):
    return [val['name'] for val in entities_geo
            if ('region' in val and val['region'] == region_id)
            and ('cat' in val and val['cat'] == ['country'])]


def get_country_by_region(pop, region_name_list):
    return [element for element in pop if (element['Area'] in region_name_list)]


def get_min_year_by_region(regions_list):
    return int(min(regions_list, key=lambda x:x['Year'])['Year'])


def get_max_year_by_region(region_list):
    return int(max(region_list, key=lambda x:x['Year'])['Year'])


def get_pop_for_region(min_year, max_year, regions_list, region_id, column_map, col_key):
    region_pop = []
    print "Calculating pop values for Europe"

    for k in column_map:
        if column_map[k] == col_key:
            col_val = k

    for year in range(min_year, max_year):
        region_pop_per_year = [val for val in regions_list if int(val['Year']) == year]
        region_per_year_sum = sum(val[col_val] for val in region_pop_per_year)

        reg_pop = dict()
        for column_key in column_map:
            if type(column_map[column_key]) is str:
                reg_pop[column_key] = column_map[column_key]
            elif column_key == 'Year':
                reg_pop['Year'] = year
            elif column_key == 'Area':
                reg_pop['Area'] = region_id
            elif column_key == col_val:
                reg_pop[col_val] = region_per_year_sum

        region_pop.append(reg_pop)

    return region_pop


# get entities based on regions (check for entries with no `regions` and `cat` value)
def get_entity_names(entities_geo):
    entities = dict()
    entities['eur'] = get_region_names(entities_geo, 'eur')
    entities['ame'] = get_region_names(entities_geo, 'ame')
    entities['afr'] = get_region_names(entities_geo, 'afr')
    entities['asi'] = get_region_names(entities_geo, 'asi')

    return entities


def get_countries_by_region(pop, entities_geo):
    regions_pop = dict()
    entity_names = get_entity_names(entities_geo)
    regions_pop['eur'] = get_country_by_region(pop, entity_names['eur'])
    regions_pop['ame'] = get_country_by_region(pop, entity_names['ame'])
    regions_pop['afr'] = get_country_by_region(pop, entity_names['afr'])
    regions_pop['asi'] = get_country_by_region(pop, entity_names['asi'])

    return regions_pop


# TODO: make them separate functions
def cal_pop_for_regions(pop, entities_geo, column_mapping, col_val):
    pop_for_region = dict()

    entity_regions_pop = get_countries_by_region(pop, entities_geo)
    min_year_eur = get_min_year_by_region(entity_regions_pop['eur'])
    max_year_eur = get_max_year_by_region(entity_regions_pop['eur'])
    pop_for_region['eur'] = get_pop_for_region(min_year_eur, max_year_eur, entity_regions_pop['eur'], 'eur', column_mapping, col_val)

    min_year_ame = get_min_year_by_region(entity_regions_pop['ame'])
    max_year_ame = get_max_year_by_region(entity_regions_pop['ame'])
    pop_for_region['ame'] = get_pop_for_region(min_year_ame, max_year_ame, entity_regions_pop['ame'], 'ame', column_mapping, col_val)

    min_year_afr = get_min_year_by_region(entity_regions_pop['afr'])
    max_year_afr = get_max_year_by_region(entity_regions_pop['afr'])
    pop_for_region['afr'] = get_pop_for_region(min_year_afr, max_year_afr, entity_regions_pop['afr'], 'afr', column_mapping, col_val)

    min_year_asi = int(min(entity_regions_pop['asi'], key=lambda x:x['Year'])['Year'])
    max_year_asi = int(max(entity_regions_pop['asi'], key=lambda x:x['Year'])['Year'])
    pop_for_region['asi'] = get_pop_for_region(min_year_asi, max_year_asi, entity_regions_pop['asi'], 'asi', column_mapping, col_val)

    return pop_for_region