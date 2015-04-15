import json


def write(file_name, data):
    with open('../data/out/waffle/' + file_name + '.json', 'w+') as outfile:
        json.dump(data, outfile, sort_keys=True, indent=4, ensure_ascii=False)
