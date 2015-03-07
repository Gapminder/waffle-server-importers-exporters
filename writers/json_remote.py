import requests
import json


def write(url, data, name, version):

    payload = json.dumps({
        'key': 'superSecretToken',
        'collection': 'waffle/examples/humnum_custom_scripts/' + name,
        'version': version,
        'name': "examples/humnum_custom_scripts",
        'data': data
    })

    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    r = requests.post(url, data=payload, headers=headers)
    print "POST for Name:", name, ", Version:", version, r.text

