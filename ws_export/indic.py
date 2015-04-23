from operator import itemgetter
import requests
from lxml import etree
import ast
import writers.xml_local
import util.name_match
import numpy


def write_indicator_file(ind_id, entity_names):
    data = {"query": '[{"SELECT": ["geo", "geo.name", "time", "' + ind_id + '"],"WHERE": {"geo": ["*"], "time":"1800-2015"},"FROM": "humnum"}]',"lang": "en"}
    r = requests.post('https://waffle.gapminder.org/api/v1/query', data=data)

    root = etree.Element('indicator')
    root.set('id', ind_id)

    all_ind_values = []
    all_min_year = []
    all_max_year = []

    data = etree.Element('data')

    ind_response = ast.literal_eval(r.content)
    countries = []

    for res in ind_response[0]:
        if res['geo'] not in countries:
            countries.append(res['geo'])

    for country in countries:
        t = etree.Element('t1')
        country_values = [element for element in ind_response[0] if element['geo'] == country]

        ind_values = [x[ind_id] for x in country_values if ind_id in x]

        if ind_values:
            min_value = min(ind_values)
            max_value = max(ind_values)

            time_values = [x['time'] for x in country_values]

            min_time = min(time_values)
            max_time = max(time_values)

            all_min_year.append(min_time)
            all_max_year.append(max_time)

            country = util.name_match.set_name_match_val(country, entity_names, 13)

            delimiter = ','
            seq = (country, str(min_value), str(max_value), str(min_time))
            m = delimiter.join(seq)
            t.set('m', m)

            d = ''
            time_sorted_country_values = sorted(country_values, key=itemgetter('time'))

            for value in time_sorted_country_values:
                if ind_id in value:
                    all_ind_values.append(float(value[ind_id]))
                    d += str(value[ind_id]) + delimiter

            t.set('d', d[:-1])
            data.append(t)

    root.append(data)

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
    root.set('dataCollectionUrl', 'N/A')
    root.set('providerSourceName', 'N/A')

    writers.xml_local.write(root, '../data/out/gw/' + ind_id + '.xml')



