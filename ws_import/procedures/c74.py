def cal_world_pop(pop, col_map, col_key):
    world_pop = []

    for k in col_map:
        if col_map[k] == col_key:
            col_val = k

    min_year = int(min(pop, key=lambda x:x['Year'])['Year'])
    max_year = int(max(pop, key=lambda x:x['Year'])['Year'])

    print "Calculating pop values for World"
    for year in range(min_year, max_year):
        pop_per_year = [val for val in pop if int(val['Year']) == year]
        pop_per_year_sum = sum(val[col_val] for val in pop_per_year)

        pop_per_year_source = [val['Source'] for val in pop]
        source = ','.join(list(set(pop_per_year_source)))

        year_pop = dict()

        for column_key in col_map:
            if type(col_map[column_key]) is str:
                year_pop[column_key] = col_map[column_key]
            elif column_key == 'Year':
                year_pop['Year'] = str(year)
            elif column_key == col_val:
                year_pop[col_val] = pop_per_year_sum
            elif column_key == 'Area':
                year_pop['Area'] = 'world'
            elif column_key == 'Source':
                year_pop['Source'] = source

        world_pop.append(year_pop)

    return world_pop