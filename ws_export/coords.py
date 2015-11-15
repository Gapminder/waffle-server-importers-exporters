import xml.etree.ElementTree as ET
import ws_export.util.name_match
import readers.excel
import writers.xml_local

xcoord = ET.parse('../data/out/gw/xml/xml_latest/XCOORDS.xml')
ycoord = ET.parse('../data/out/gw/xml/xml_latest/YCOORDS.xml')

country_synonym_list = readers.excel.read('../data/synonym/country_synonyms.xlsx', 0, None)
country_synonym = country_synonym_list[0]
entity_names = [[0 for x in range(0, country_synonym.ncols)] for x in range(1, country_synonym.nrows)]

for r_num in range(1, country_synonym.nrows):
    for c_num in range(0, country_synonym.ncols):
        entity_names[r_num - 1][c_num] = country_synonym.cell_value(rowx=r_num, colx=c_num)


x_data = xcoord.findall('data/t5')
y_data = ycoord.findall('data/t5')

for x_point in x_data:
    ini_name = x_point.get('m')
    x_point.set('m', ws_export.util.name_match.set_name_match_val(ini_name, entity_names,13))

for y_point in y_data:
    ini_name = y_point.get('m')
    y_point.set('m', ws_export.util.name_match.set_name_match_val(ini_name, entity_names, 13))


#writers.xml_local.write(xcoord, 'xcoord.xml')
xcoord.write('XCOORDS.xml')
ycoord.write('YCOORDS.xml')




