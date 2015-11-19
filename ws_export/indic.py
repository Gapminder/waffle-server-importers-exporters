from operator import itemgetter
import collections
from lxml import etree
import writers.xml_local
import util.name_match
import numpy
import readers.json_reader
import readers.excel




def write_indicator_file(ind_id, entity_names):
    print ind_id
    ind_response = readers.json_reader.read('../data/out/gw/indicators/' + str(ind_id) + '.json')
    synonym_map = readers.json_reader.read('../data/synonym/synonym_map.json')

    root = etree.Element('indicator')
    root.set('id', ind_id)

    all_ind_values = []
    all_min_year = []
    all_max_year = []

    data = etree.Element('data')
    countries = []

    for res in ind_response:
        if res['geo'] not in countries:
            countries.append(res['geo'])

    for country in countries:
        print country
        if country == 'i144':
            print country

        t = etree.Element('t1')
        country_values = [element for element in ind_response if element['geo'] == country]

        country = util.name_match.set_name_match_val(country, entity_names, 13)

        ind_values = [x[ind_id] for x in country_values if ind_id in x]

        if ind_values:
            min_value = min(ind_values)
            max_value = max(ind_values)

            time_values = [x['time'] for x in country_values]

            min_time = min(time_values)
            max_time = max(time_values)

            all_min_year.append(min_time)
            all_max_year.append(max_time)

            delimiter = ','
            seq = (country, str(min_value), str(max_value), str(int(min_time)))
            m = delimiter.join(seq)
            t.set('m', m)

            d = ''
            time_sorted_country_values = sorted(country_values, key=itemgetter('time'))
            # multiple countries with same name

            increment = 1
            for el in synonym_map:
                if country in el:
                    for item_list in el[country]:
                        for item in item_list:
                            if ind_id in item:
                                increment = item_list[ind_id]


            k = 0
            #k = next(index for (index, d) in enumerate(country_values) if d["time"] == min_time)
            i = min_time
            #while i < max_time:
            while i <= max_time:
                #for value in time_sorted_country_values:
                while k < len(time_sorted_country_values):
                    value = time_sorted_country_values[k]
                    ind_value = value[ind_id]
                    #print country
                    try:
                        float(ind_value)
                        valid_value = True
                    except ValueError:
                        valid_value = False

                    #if ind_id in value and value['time'] == i:
                    #if ind_id in value and value['time'] == i and (type(value[ind_id]) is float
                    #                                               or type(value[ind_id]) is int):
                    if ind_id in value and value['time'] == i and valid_value:
                        indicator_value = float(ind_value)
                        all_ind_values.append(indicator_value)
                        #d += str(value[ind_id]) + delimiter
                        d += ind_value + delimiter
                        #k += 1
                        k += increment
                    else:
                        j = i
                        counter = 0
                        while value['time'] != j:
                            counter += 1
                            j += 1

                        if counter == 1:
                            d += delimiter
                        else:
                            d += 'n' + str(counter) + delimiter
                        i = j - 1
                    i += 1
            t.set('d', d[:-1])
            data.append(t)

    root.append(data)

    if len(all_ind_values) > 0:
        root.set('min', str(min(all_ind_values)))
        root.set('max', str(max(all_ind_values)))
        root.set('first_time', str(min(all_min_year)))
        root.set('last_time', str(max(all_max_year)))

        mean_val = numpy.mean(all_ind_values)
        median_val = numpy.median(all_ind_values)

        post_ind_values = [e for e in all_ind_values if e > 0]
        neg_ind_values = [e for e in all_ind_values if e < 0]

        if abs(mean_val - median_val) > 2 * mean_val:
            root.set('scale', 'log')
            if not neg_ind_values:
                root.set('closestBelowZero', str(max(neg_ind_values)))
            else:
                root.set('closestBelowZero', '0')

        else:
            root.set('scale', 'lin')
            root.set('closestBelowZero', '0')

        root.set('closestAboveZero', str(min(post_ind_values)))
        root.set('dataCollectionUrl', 'http://spreadsheets.google.com/pub?key=' + ind_id + '&gid=1')
        root.set('providerUrl', 'http://spreadsheets.google.com/pub?key=' + ind_id + '&gid=1')
        root.set('providerSourceName', 'Source(s)')
    else:
        root.set('min', '1.7976931348623157E308')
        root.set('max', '-1.7976931348623157E308')
        root.set('first_time', '2147483647')
        root.set('last_time', '-2147483648')
        root.set('closestBelowZero', '0.0')
        root.set('scale', 'lin')
        root.set('closestAboveZero', '0.0')

        root.set('dataCollectionUrl', 'http://spreadsheets.google.com/pub?key=' + ind_id + '&gid=1')
        root.set('providerUrl', 'http://spreadsheets.google.com/pub?key=' + ind_id + '&gid=1')
        root.set('providerSourceName', 'Source(s)')

    writers.xml_local.write(root, '../data/out/gw/xml/' + ind_id + '.xml')
    print 'write to file: ' + '../data/out/gw/xml/' + ind_id + '.xml'


country_synonym_list = readers.excel.read('../data/synonym/country_synonyms.xlsx', 0, None)
country_synonym = country_synonym_list[0]
entity_names = [[0 for x in range(0, country_synonym.ncols)] for x in range(1, country_synonym.nrows)]


#UNCOMMENT HERE: write_indicator_file("0ArfEDsV3bBwCdGhSY2trbEVpYnNsMENqendaVm5ucnc", entity_names)


