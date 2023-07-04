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
        self.assertEqual(parse_coom('behavior{require a = b}'), [
            'behavior((":root",0)).', 'require((":root",0),"a=b").',
            'binary(":root","a=b","a","=","b").', 'path("a",0,"a").',
            'path("b",0,"b").'
        ])

        self.assertEqual(
            parse_coom(
                'behavior {condition color = Yellow require frontWheel.size > 16}'
            ), [
                'behavior((":root",0)).',
                'condition((":root",0),"color=Yellow").',
                'binary(":root","color=Yellow","color","=","Yellow").',
                'path("color",0,"color").', 'path("Yellow",0,"Yellow").',
                'require((":root",0),"frontWheel.size>16").',
                'binary(":root","frontWheel.size>16","frontWheel.size",">","16").',
                'path("frontWheel.size",0,"frontWheel").',
                'path("frontWheel.size",1,"size").'
            ])
        self.assertEqual(
            parse_coom('''behavior {
                            combinations  (wheelSupport	 rearWheel)
                            allow         (True          (W14, W16))
                            allow         (False         (W18, W20))}'''), [
                'behavior((":root",0)).',
                'combinations((":root",0),0,"wheelSupport").',
                'combinations((":root",0),1,"rearWheel").',
                'path("wheelSupport",0,"wheelSupport").',
                'path("rearWheel",0,"rearWheel").',
                'allow((":root",0),(0,0),"True").',
                'allow((":root",0),(1,0),"W14").',
                'allow((":root",0),(1,0),"W16").',
                'allow((":root",0),(0,1),"False").',
                'allow((":root",0),(1,1),"W18").',
                'allow((":root",0),(1,1),"W20").'
            ])

        self.assertEqual(parse_coom('behavior{require a = b require c = d}'), [
            'behavior((":root",0)).', 'require((":root",0),"a=b").',
            'binary(":root","a=b","a","=","b").', 'path("a",0,"a").',
            'path("b",0,"b").', 'behavior((":root",1)).',
            'require((":root",1),"c=d").',
            'binary(":root","c=d","c","=","d").', 'path("c",0,"c").',
            'path("d",0,"d").'
        ])

    def test_multiplicity(self):
        pass


if __name__ == '__main__':
    unittest.main()
