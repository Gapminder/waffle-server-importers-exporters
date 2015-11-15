import readers.excel
import ws_export.util
import util.url
import ws_export.util.name_match
import ws_import.procedures.gw.synonyms
import readers.json_reader


def get(about):
    entity_names = ws_import.procedures.gw.synonyms.get_entity_synonyms()
    area_categorization = []
    if about.cell_value(rowx=0, colx=1) == 'Gapminder World':
        color_groups = readers.excel.read('../../data/meta/graph_settings.xlsx', None, 'Color groups')[0]
        group_ids = readers.json_reader.read('../../data/synonym/area_id.json')

        for rx in range(1, color_groups.nrows):
            group_id = (el['id'] for el in group_ids if el['name'] == color_groups.cell_value(rx, colx=0)).next()
            group = {'id': group_id,
                     'n': color_groups.cell_value(rx, colx=0),
                     'a': color_groups.cell_value(rx, colx=1),
                     'sourceName': color_groups.cell_value(rx, colx=2),
                     'providerUrl': color_groups.cell_value(rx, colx=2)}

            util.url.save_remote_spreadsheet(group['providerUrl'], '../../data/meta/' + group['n'] + '.xlsx')

            group['dataCollectionUrl'] = color_groups.cell_value(rowx=rx, colx=2)
            group['groupings'] = {}

            groups = readers.excel.read('../../data/meta/' + group['n'] + '.xlsx', None, 'Groups')[0]

            for rowx in range(1, groups.nrows):
                group_name = ws_export.util.name_match.set_name_match_val_region(groups.cell_value(rowx=rowx, colx=1))
                if group_name is not '':
                    if group_name not in group['groupings']:
                        group['groupings'][group_name] = []
                    name_match_id = ws_export.util.name_match.set_name_match_val(groups.cell_value(rowx=rowx, colx=0), entity_names, 13)
                    group['groupings'][group_name].append(name_match_id)

            area_categorization.append(group)

    return area_categorization