from lxml import etree


def write(root, path):
    et = etree.ElementTree(root)
    et.write(path, encoding='UTF-8', pretty_print=True)
