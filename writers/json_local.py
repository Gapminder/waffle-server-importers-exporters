import json


def write(path, file_name, data):
    with open(path + file_name + '.json', 'w+') as outfile:
        print "write to file:" + path + file_name + '.json'
        json.dump(data, outfile, sort_keys=True, indent=4, ensure_ascii=False)
