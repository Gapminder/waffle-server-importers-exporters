import numpy
import requests


def write(url, data, name, version):
    datum = numpy.asarray(data)
    post_data = {
        'key': 'superSecretToken',
        'collection': 'waffle/examples/humnum_custom_scripts/' + name,
        'version': version,
        'name': "examples/humnum_custom_scripts",
        "data": datum
    }

    r = requests.post(url, data=post_data)
    print "POST for Name:", name, ", Version:", version, r.text

