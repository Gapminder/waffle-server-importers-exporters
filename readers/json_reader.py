import json


def read(source):
    json_data = open(source)
    data = json.load(json_data)
    for d in data:
        if 'name' in d:
            d['name'] = d['name'].encode('utf-8')
    json_data.close()

    return data
