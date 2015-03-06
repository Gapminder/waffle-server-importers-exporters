def map_keys_pop(pop, map_keys):

    for element in pop:
        for key in map_keys:
            element[map_keys[key]] = element[key]
            del element[key]

    return pop