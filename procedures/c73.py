# TODO: remove references to `Area`, `Population`
# TODO: move hard-coded values


def cal_pop_country_values(pop_list, pop_version):
    pop = []

    for r_num in range(1, pop_list.nrows):
        country = dict()
        if pop_list.cell_value(rowx=r_num, colx=3) != "":
            country['Area'] = pop_list.cell_value(rowx=r_num, colx=0)
            country['Population'] = pop_list.cell_value(rowx=r_num, colx=2)
            country['Population with interpolations'] = pop_list.cell_value(rowx=r_num, colx=3)
            country['Year'] = pop_list.cell_value(rowx=r_num, colx=1)
            country['dim'] = 'geo-time'
            country['version'] = pop_version
            pop.append(country)

    return pop