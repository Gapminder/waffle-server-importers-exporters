# TODO: remove references to `Area`, `Population`
# TODO: move hard-coded values
from types import IntType


def cal_pop_country_values(pop_list, col_map, value_key_num):
    pop = []

    for r_num in range(1, pop_list.nrows):
        country = dict()

        if pop_list.cell_value(rowx=r_num, colx=value_key_num) != "":
            for col_key in col_map:
                if type(col_map[col_key]) is IntType:
                    country[col_key] = pop_list.cell_value(rowx=r_num, colx=col_map[col_key])
                else:
                    country[col_key] = col_map[col_key]
            pop.append(country)

    return pop