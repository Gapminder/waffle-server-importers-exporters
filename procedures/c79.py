def map_keys_pop(pop):
    for element in pop:
        element['time'] = element['Year']
        del element['Year']
        element['geo'] = element['Area']
        del element['Area']
        element['pop'] = element['Population with interpolations']
        del element['Population with interpolations']

    return pop