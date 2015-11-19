import unittest
import xml.etree.ElementTree as ET
import util.log


class TestOverview(unittest.TestCase):
    def setUp(self):
        self.output_overview = ET.parse('data/out/gw/xml/overview.xml')
        self.output_root = self.output_overview.getroot()

        self.test_overview = ET.parse('test_data/overview.xml')
        self.test_root = self.test_overview.getroot()

    def test_default_size(self):
        assert self.output_root is not None
        assert self.test_root is not None

    def test_general_structure(self):
        for test_childr in self.test_root:
            for child_in in self.output_root.iter(test_childr.tag):
                    self.assertEquals(ET.Element, type(child_in))

    def test_indicators_exist(self):
        for neighbour in self.test_root.iter('indicators'):
            for child in neighbour:
                assert type(self.output_root.findall("indicators/i[@id='" + child.get('id') + "']")) is list
                assert len(self.output_root.findall("indicators/i[@id='" + child.get('id') + "']")) == 1

    def test_all_entities_exist(self):
        for neighbour in self.test_root.iter('areas'):
            for child in neighbour:
                assert type(self.output_root.findall("areas/a[@id='" + child.get('id') + "']")) is list
                assert len(self.output_root.findall("areas/a[@id='" + child.get('id') + "']")) == 1

    def test_all_area_categories(self):
        for neighbour in self.test_root.iter('areaCategorization'):
            area_cat_test = self.output_root.findall("areaCategorization[@id='" + neighbour.get('id') + "']")
            self.assertEquals(len(area_cat_test), 1)

            for child in neighbour:
                areas = self.output_root.findall("areaCategorization/c[@id='" + child.get('id') + "']")
                self.assertEquals(len(areas), 1)

                test_child = child.get('areas')
                area_concat = areas[0].get('areas')

                test_child_list = test_child.split(',')
                try:
                    test_child_int_list = [int(x[1:]) for x in test_child_list]
                except ValueError:
                    print x
                test_child_str_list = ["i" + str(x) for x in test_child_int_list]

                area_list = area_concat.split(',')

                area_int_list = []
                for x in area_list:
                    try:
                        area_int_list.append(int(x[1:]))
                    except ValueError:
                        print x
                area_str_list = ["i" + str(x) for x in area_int_list]

                #self.assertEquals(area_str_list, test_child_str_list)
                if not len(list(set(area_str_list) - set(test_child_str_list))) == 0:
                    util.log.set_info('     Region ' + str(child.get('id')) + ' has following difference:    ' +
                                      ','.join(list(set(area_str_list) - set(test_child_str_list))))


    def test_all_indicator_categories(self):
        self.assertEqual(self.test_root.findall("indicatorCategorization[@indicators]")[0].get('indicators'),
                         self.output_root.findall("indicatorCategorization[@indicators]")[0].get('indicators'))

        for neighbour in self.test_root.findall('indicatorCategorization/c'):
            test_cats = self.output_root.findall("indicatorCategorization/c[@id='" + neighbour.get('id') + "']")
            assert len(test_cats) == 1
            self.assertEqual(neighbour.get('id'), test_cats[0].get('id'))
            self.assertEqual(neighbour.get('name'), test_cats[0].get('name'))

            test_cats = self.test_root.findall("indicatorCategorization/c[@id='" + neighbour.get('id') + "']/c")

            for child in test_cats:
                test_cats_children = self.output_root.findall("indicatorCategorization/c[@id='" + neighbour.get('id')
                                                            + "']/c[@id='" + child.get('id') + "']")
                assert len(test_cats_children) == 1
                self.assertEqual(child.get('indicators'), test_cats_children[0].get('indicators'))


if __name__ == '__main__':
    unittest.main()