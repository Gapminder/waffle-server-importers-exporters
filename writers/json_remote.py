import requests
import json


def write(url, data, name, version):

    payload = json.dumps({
        'key': 'superSecretToken',
        'collection': 'waffle/examples/wsie/' + name,
        'version': version,
        'name': "examples/wsie",
        'data': data
    })

    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    r = requests.post(url, data=payload, headers=headers)
    print "POST for Name:", name, ", Version:", version, r.text

