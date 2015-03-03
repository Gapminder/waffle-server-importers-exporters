def cal_world_pop(pop, pop_version):
    world_pop = []

    min_year = int(min(pop, key=lambda x:x['Year'])['Year'])
    max_year = int(max(pop, key=lambda x:x['Year'])['Year'])

    print "Calculating pop values for World"
    for year in range(min_year, max_year):
        pop_per_year = [val for val in pop if int(val['Year']) == year]
        pop_per_year_sum = sum(val['Population with interpolations'] for val in pop_per_year)

        year_pop = dict()
        year_pop['Version'] = pop_version
        year_pop['Population with interpolations'] = pop_per_year_sum
        year_pop['Source'] = ['No data']
        year_pop['Area'] = 'world'
        year_pop['Year'] = year

        world_pop.append(year_pop)

    return world_pop