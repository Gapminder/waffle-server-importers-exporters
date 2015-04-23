import ConfigParser


config = ConfigParser.ConfigParser()
config.read('../../config.cfg')
url = config.get('URL', 'waffle')


def get_value(section, attr):
    """Return value of an attribute in a section of config file"""
    return config.get(section, attr)


