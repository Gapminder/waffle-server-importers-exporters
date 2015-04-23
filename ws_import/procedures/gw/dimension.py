def get(indicators):
    """Write the dimension in the data to remote
        Note that this is a temporary fix
    """
    dim = []

    for rx in range(1, indicators.nrows):
        indicator_url = indicators.cell_value(rowx=rx, colx=4)
        key_index = indicator_url.find('key=') + 4
        indicator_id = indicator_url[key_index:]

        dim_t = {'-t-id': indicator_id, '-t-dim': indicator_id, '-t-kind': 'dim'}
        dim.append(dim_t)

    return dim