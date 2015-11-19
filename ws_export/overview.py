#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ast;import requests
import util.name_match
import writers.xml_local
import ws_export.indic
import readers.json_reader
import readers.excel
import ws_export.util.name_match
import collections

from lxml import etree



def hard_code_entity(area):
    a = etree.Element('a')
    a.set('id', unicode(area['id']))
    a.set('n', unicode(area['name']))

    return a

def write_overview_indicator(entity_names):
    root = etree.Element('metadata')

    map_properties = etree.Element('mapProperties')
    root.append(map_properties)

    map_properties.set('imageFile', 'http://www.gapminderdev.org/GapminderMedia/wp-uploads/gapminder-world/map.jpg')
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

    ind_responses = readers.json_reader.read('data/out/gw/meta/quantities.json')

    for ind in ind_responses:
        ws_export.indic.write_indicator_file(ind['-t-ind'], entity_names)

        i = etree.Element('i')
        i.set('id', ind['-t-ind'])
        i.set('displayName', ind['-t-name'])
        i.set('originalName', ind['-t-name'])
        indicators.append(i)

    root.append(indicators)

    area_sheet = readers.excel.read('data/synonym/country_synonyms.xlsx', 0, None)[0]
    area_response = []

    for rox in range(1, area_sheet.nrows):
        entity_name = area_sheet.cell_value(rowx=rox, colx=1)
        entity_id = area_sheet.cell_value(rowx=rox, colx=13)


        if entity_name and entity_id:
            area_o = {'name': entity_name, 'id': entity_id}
            area_response.append(area_o)

    areas = etree.Element('areas')
    area_response.append({'id': 'i263', 'name': 'America'})
    area_response.append(({'id': 'i279', 'name': 'Christian'}))
    area_response.append({'id': 'i270', 'name': 'Coastline'})
    area_response.append({'id': 'i265', 'name': 'East Asia &amp; Pacific'})
    area_response.append({'id': 'i281', 'name': 'Eastern religions'})
    area_response.append({'id': 'i264', 'name': 'Europe &amp; Central Asia'})
    area_response.append({'id': 'i272', 'name': 'G77'})
    area_response.append({'id': 'i268', 'name': 'High income'})
    area_response.append({'id': 'i271', 'name': 'Landlocked'})
    area_response.append({'id': 'i266', 'name': 'Low income'})
    area_response.append({'id': 'i269', 'name': 'Lower middle income'})
    area_response.append({'id': 'i262', 'name': 'Middle East &amp; North Africa'})
    area_response.append({'id': 'i273', 'name': 'OECD'})

    area_response.append({'id': 'i274', 'name': 'Others'})
    area_response.append({'id': 'i261', 'name': 'South Asia'})
    area_response.append({'id': 'i260', 'name': 'Sub-Saharan Africa'})
    area_response.append({'id': 'i267', 'name': 'Upper middle income'})
    area_response.append({'id':  'i280', 'name': 'Muslim'})

    area_response.append({'id': 'i277', 'name': '[Africa]'})
    area_response.append({'id': 'i278', 'name': '[America]'})
    area_response.append({'id': 'i276', 'name': '[Asia]'})
    area_response.append({'id': 'i275', 'name': '[Europe]'})

    area_response_sorted = sorted(area_response, key=lambda area: area['name'])

    for area in area_response_sorted:
        a = etree.Element('a')
        a.set('id', unicode(area['id']))
        a.set('n', unicode(area['name']))

        areas.append(a)

    root.append(areas)

    area_cat = readers.json_reader.read('data/out/gw/meta/area_categorizarion.json')

    for cat in area_cat:
        areas = etree.Element('areaCategorization')
        areas.set('id', cat['id'])
        areas.set('n', cat['n'])
        areas.set('a', cat['a'])
        areas.set('sourceName', cat['a'])
        areas.set('providerUrl', cat['providerUrl'])
        areas.set('dataCollectionUrl', cat['dataCollectionUrl'])


        keylist = cat['groupings'].keys()
        keylist.sort()

        for key in keylist:
            c = etree.Element('c')
            c.set('id', key)
            c.set('areas', ','.join(cat['groupings'][key]))
            areas.append(c)
        root.append(areas)


    ind_cat = readers.json_reader.read('data/out/gw/meta/indicator_categorizarion.json')

    inds = etree.Element('indicatorCategorization')
    inds.set('indicators', ','.join(ind_cat['indicators']))
    for cats in ind_cat['categories']:
        c = etree.Element('c')

        c.set('n', cats)
        c.set('id', cats)
        if len(ind_cat['categories'][cats]['indicators']) != 0:
            c.set('indicators', ','.join(ind_cat['categories'][cats]['indicators']))

        for cat in ind_cat['categories'][cats]:
            c_2 = etree.Element('c')
            c_2.set('n',  cat)
            c_2.set('id', cat)
            c_2.set('indicators', ','.join(ind_cat['categories'][cats][cat]))
            c.append(c_2)
        inds.append(c)
    root.append(inds)

    writers.xml_local.write(root, 'data/out/gw/xml/overview.xml')
