import json


def read(source):
    json_data = open(source)
    data = json.load(json_data)
    json_data.close()

    return data
