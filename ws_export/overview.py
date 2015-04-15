import ast
import requests
import util.name_match
import writers.xml_local
import ws_export.indic

from lxml import etree


def write_overview_indicator(entity_names):
    # TODO: Change Query to following once importers are in place
    # data = {'query': '[{"SELECT": ["*"], "WHERE": {"quantity": ["*"]}, "FROM": "humnum"}]', 'lang': 'en'}
    data = {'query': '[{"SELECT": ["*"], "WHERE": {"quantity": ["pop"]}, "FROM": "humnum"}]', 'lang': 'en'}
    r = requests.post('https://waffle.gapminder.org/api/v1/query', data=data)

    root = etree.Element('metadata')

    map_properties = etree.Element('mapProperties')
    root.append(map_properties)

    map_properties.set('ImageFile', 'http://www.gapminder.org/GapminderMedia/wp-uploads/gapminder_world/gw-map.jpg')
    map_properties.set('timeDisplayX', '0')
    map_properties.set('timeDisplayY', '0')
    map_properties.set('scaleImage', 'true')

    collection_info = etree.Element('collectionInfo')
    root.append(collection_info)

    caption = etree.Element('caption')
    caption.set('url', 'http://www.gapminder.org')
    caption.text = 'Gapminder World'

    collection_info.append(caption)

    indicators = etree.Element('indicators')

    ind_response = ast.literal_eval(r.content)

    for ind in ind_response[0]:
        ws_export.indic.write_indicator_file(ind['-t-ind'], entity_names)

        i = etree.Element('i')
        i.set('id', ind['-t-ind'])
        i.set('displayName', ind['-t-name'])
        i.set('originalName', ind['-t-name'])
        indicators.append(i)

    root.append(indicators)

    entity_data = {'query': '[{"SELECT": ["*"],"WHERE": {"geo": "*", "geo.cat": ["country"]}, "FROM": "humnum"}]', 'lang': 'en'}

    r = requests.post('https://waffle.gapminder.org/api/v1/query', data=entity_data)

    area_response = ast.literal_eval(r.content)

    areas = etree.Element('areas')
    for area in area_response[0]:
        country = util.name_match.set_name_match_val(area['id'], entity_names)

        a = etree.Element('a')
        a.set('id', country)

        name = area["name"].decode(encoding='UTF-8', errors='strict')
        a.set('n', name)

        areas.append(a)

    root.append(areas)
    writers.xml_local.write(root, '../data/out/gw/overview.xml')
