def get(indicators):
    """Write the  quantities in the data to remote
        Note that this is a temporary fix
    """
    quantities = []

    for rx in range(1, indicators.nrows):
        indicator_name = indicators.cell_value(rowx=rx, colx=0)
        indicator_url = indicators.cell_value(rowx=rx, colx=4)
        key_index = indicator_url.find('key=') + 4
        indicator_id = indicator_url[key_index:]

        quantities_t = {'-t-ind': indicator_id, '-t-name': indicator_name, '-t-types': '{}'}
        quantities.append(quantities_t)

    return quantities


