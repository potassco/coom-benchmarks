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


if __name__ == '__main__':
    unittest.main()
