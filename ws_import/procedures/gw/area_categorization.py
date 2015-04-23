import readers.excel
import ws_export.util
import util.url
import ws_export.util.name_match
import ws_import.procedures.gw.synonyms

def get(about):
    entity_names = ws_import.procedures.gw.synonyms.get_entity_synonyms()
    area_categorization = []
    if about.cell_value(rowx=0, colx=1) == 'Gapminder World':
        color_groups = readers.excel.read('../../data/meta/graph_settings.xlsx', None, 'Color groups')[0]
        for rx in range(1, color_groups.nrows):
            group = {'id': 'CATID' + str(rx),
                     'n': color_groups.cell_value(rx, colx=0),
                     'a': color_groups.cell_value(rx, colx=1),
                     'sourceName': color_groups.cell_value(rx, colx=2),
                     'provideUrl': color_groups.cell_value(rx, colx=2)}

            util.url.save_remote_spreadsheet(group['provideUrl'], '../../data/meta/' + group['n'] + '.xlsx')

            group['dataCollectionUrl'] = color_groups.cell_value(rowx=1, colx=1)
            group['groupings'] = {}

            groups = readers.excel.read('../../data/meta/' + group['n'] + '.xlsx', None, 'Groups')[0]

            for rowx in range(1, groups.nrows):
                group_name = groups.cell_value(rowx=rowx, colx=1)
                if group_name in group['groupings']:
                    print rowx
                    name_match_id = ws_export.util.name_match.set_name_match_val(groups.cell_value(rowx=rowx, colx=0), entity_names, 13)
                    group['groupings'][group_name].append({
                        'id': name_match_id
                    })
                else:
                    group['groupings'][group_name] = []

            area_categorization.append(group)

    return area_categorization