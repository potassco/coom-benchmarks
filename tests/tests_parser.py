"""
Tests checking the parser from COOM to ASP.
"""
from tests import parse_coom
import unittest


class TestMain(unittest.TestCase):

    def test_product(self):
        self.assertEqual(parse_coom('product{}'), ['structure(":root").'])

    def test_structure(self):
        self.assertEqual(parse_coom('structure Test {}'),
                         ['structure("Test").'])

    def test_feature(self):
        self.assertEqual(parse_coom('product{Wheel wheel Frame frame}'), [
            'structure(":root").', 'feature(":root","wheel","Wheel",1,1).',
            'feature(":root","frame","Frame",1,1).'
        ])

    def test_enumeration(self):
        self.assertEqual(
            parse_coom('enumeration Color {Red Green Yellow Blue}'), [
                'enumeration("Color").', 'option("Color", "Red").',
                'option("Color", "Green").', 'option("Color", "Yellow").',
                'option("Color", "Blue").'
            ])
        self.assertEqual(
            parse_coom('''\
                enumeration Capacity {
                        attribute num/l volume
                        attribute num/gr weight
                        B10  = ( 10,  100)
                        B20  = ( 20,  250)
                    }'''), [
                'enumeration("Capacity").', 'attribute("Capacity","volume").',
                'attribute("Capacity","weight").',
                'option("Capacity", "B10").',
                'value("Capacity","B10","volume",10).',
                'value("Capacity","B10","weight",100).',
                'option("Capacity", "B20").',
                'value("Capacity","B20","volume",20).',
                'value("Capacity","B20","weight",250).'
            ])

    def test_behavior(self):
        self.assertEqual(parse_coom('behavior{require a = b}'), ['behavior((":root",0))'])

    def test_multiplicity(self):
        pass


if __name__ == '__main__':
    unittest.main()
