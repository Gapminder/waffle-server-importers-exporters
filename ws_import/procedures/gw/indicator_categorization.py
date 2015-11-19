import readers.excel


def get(callback):
    indicator_categorization = {'indicators': [], 'categories': {}}
    indicators = readers.excel.read('data/meta/graph_settings.xlsx', None, 'Indicators')[0]

    for rx in range(1, indicators.nrows):
        indicator_url = indicators.cell_value(rowx=rx, colx=4)
        key_index = indicators.cell_value(rowx=rx, colx=4).find('key=') + 4

        menu_level = indicators.cell_value(rowx=rx, colx=2)
        menu_level_two = indicators.cell_value(rowx=rx, colx=3)
        if not menu_level and not menu_level_two:
            indicator_categorization['indicators'].append(indicator_url[key_index:])
        elif menu_level not in indicator_categorization['categories']:
            indicator_categorization['categories'][menu_level] = {'indicators': []}
            indicator_categorization['categories'][menu_level][menu_level_two] = []
            indicator_categorization['categories'][menu_level][menu_level_two].append(indicator_url[key_index:])
        elif menu_level in indicator_categorization['categories'] and not menu_level_two:
            indicator_categorization['categories'][menu_level]['indicators'].append(indicator_url[key_index:])
        elif menu_level in indicator_categorization['categories'] and menu_level_two not in indicator_categorization['categories'][menu_level]:
            indicator_categorization['categories'][menu_level][menu_level_two] = []
            indicator_categorization['categories'][menu_level][menu_level_two].append(indicator_url[key_index:])
        else:
            indicator_categorization['categories'][menu_level][menu_level_two].append(indicator_url[key_index:])
        #callback(indicator_url=indicator_url, indicator_id=indicator_url[key_index:])


    return indicator_categorization