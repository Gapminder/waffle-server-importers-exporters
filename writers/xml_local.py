from lxml import etree


def write(root, path):
    # pretty string
    et = etree.ElementTree(root)
    et.write(path, pretty_print=True)
