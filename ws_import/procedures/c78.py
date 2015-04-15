def calc_merge_pop(pop_regions, world_pop, pop):
    merged_pop = []

    for pop_region in pop_regions:
        merged_pop += pop_regions[pop_region]
    merged_pop += pop + world_pop

    return merged_pop