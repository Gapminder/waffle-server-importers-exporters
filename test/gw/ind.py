import unittest
import xml.etree.ElementTree as ET
import readers.excel
import logging

logging.basicConfig(filename='indicator_file_check_11_may_15:39.log', level=logging.DEBUG)


class TestIndicators(unittest.TestCase):

    def __init__(self, test_name, indicator, test_indicator):
        super(TestIndicators, self).__init__(test_name)
        self.output_root = indicator.getroot()
        self.test_root = test_indicator.getroot()

    def test_indicator_root(self):
        for attr in self.output_root:
            assert self.output_root.get(attr) is self.test_root.get(attr)

    def test_indicator_data(self):
        data_tag = self.output_root.findall('data/t1')
        data_tag_test = self.test_root.findall('data/t1')
        count = 0

        for tag in data_tag:
            m = tag.get('m').split(',')
            for test_tag in data_tag_test:
                m_test = test_tag.get('m').split(',')
                if m[0] == m_test[0]:
                    # TODO: fix in the data
                    m[3] = str(int(float(m[3])))

                    d = tag.get('d').split(',')
                    for i in range(0, len(d)):
                        try:
                            d[i] = format(float(d[i]), '.4g')
                            #d[i] = "{0:.1f}".format(d[i])
                        except ValueError:
                            print ""

                    d_test = test_tag.get('d').split(',')
                    for i in range(0, len(d_test)):
                        try:
                            d_test[i] = format(float(d_test[i]), '.4g')
                            #d_test[i] = "{0:.1f}".format(d_test[i])
                        except ValueError:
                            print ""

                    if d != d_test:
                        logging.warning('COUNTRY: ' + str(m[0]) + ' data was not equal compared to the test')
                        count += 1
                        #logging.warning('YEARS that the data is not equal in comparison')

                        #if len(d) == len(d_test):
                        #    for i in range(0, len(d)):
                        #        if d[i] != d_test[i]:
                        #            logging.warning("YEAR: " + str(i + float(m[3])))




        logging.info('----------------------------------------------')
        logging.info('----------------------------------------------')
        logging.info('NUMBER OF SUCCESSFUL TESTS:' + str(len(data_tag) - count))


if __name__ == '__main__':
    indicators = readers.excel.read('../../data/meta/graph_settings.xlsx', None, 'Indicators')[0]

    for rx in range(1, indicators.nrows):
        suite = unittest.TestSuite()
        indicator_url = indicators.cell_value(rowx=rx, colx=4)
        key_index = indicators.cell_value(rowx=rx, colx=4).find('key=') + 4
        indicator_id = indicator_url[key_index:]

        logging.info('\n\nTEST RESULT FOR INDICATOR FILE:' + indicator_id)

        indicator = ET.parse('../../data/out/gw/xml/' + indicator_id + '.xml')
        test_indicator = ET.parse('test_data/' + indicator_id + '.xml')
        suite.addTest(TestIndicators("test_indicator_root", indicator, test_indicator))
        suite.addTest(TestIndicators("test_indicator_data", indicator, test_indicator))

        logging.info('----------------------------------------------')
        logging.info('----------------------------------------------')

        unittest.TextTestRunner().run(suite)





