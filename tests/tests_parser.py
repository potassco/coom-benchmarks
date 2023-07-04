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

        self.assertEqual(
            parse_coom('structure Carrier {0..3 Bag bags}'),
            ['structure("Carrier").', 'feature("Carrier","bags","Bag",0,3).'])

        self.assertEqual(parse_coom('structure Carrier {2..* Bag bags}'), [
            'structure("Carrier").', 'feature("Carrier","bags","Bag",2,#sup).'
        ])

        self.assertEqual(
            parse_coom('structure Carrier {5x Bag bags}'),
            ['structure("Carrier").', 'feature("Carrier","bags","Bag",5,5).'])

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

        self.assertEqual(parse_coom('behavior Bag {require a = b}'), [
            'behavior(("Bag",0)).', 'require(("Bag",0),"a=b").',
            'binary("Bag","a=b","a","=","b").', 'path("a",0,"a").',
            'path("b",0,"b").'
        ])

        self.assertEqual(parse_coom('behavior {default color = red}'), [
            'behavior((":root",0)).', 'default((":root",0),"color","red").',
            'path("color",0,"color").', 'path("red",0,"red").'
        ])

        self.assertEqual(parse_coom('behavior{require a = b require c = d}'), [
            'behavior((":root",0)).', 'require((":root",0),"a=b").',
            'binary(":root","a=b","a","=","b").', 'path("a",0,"a").',
            'path("b",0,"b").', 'behavior((":root",1)).',
            'require((":root",1),"c=d").',
            'binary(":root","c=d","c","=","d").', 'path("c",0,"c").',
            'path("d",0,"d").'
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

        self.assertEqual(
            parse_coom('''behavior Bike {
                            combinations  (wheelSupport	 rearWheel)
                            allow         (True          (W14, W16))
                            allow         (False         (W18, W20))}'''), [
                'behavior(("Bike",0)).',
                'combinations(("Bike",0),0,"wheelSupport").',
                'combinations(("Bike",0),1,"rearWheel").',
                'path("wheelSupport",0,"wheelSupport").',
                'path("rearWheel",0,"rearWheel").',
                'allow(("Bike",0),(0,0),"True").',
                'allow(("Bike",0),(1,0),"W14").',
                'allow(("Bike",0),(1,0),"W16").',
                'allow(("Bike",0),(0,1),"False").',
                'allow(("Bike",0),(1,1),"W18").',
                'allow(("Bike",0),(1,1),"W20").'
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
            parse_coom(
                'behavior {condition material = Leather default capacity = B10}'
            ), [
                'behavior((":root",0)).',
                'condition((":root",0),"material=Leather").',
                'binary(":root","material=Leather","material","=","Leather").',
                'path("material",0,"material").',
                'path("Leather",0,"Leather").',
                'default((":root",0),"capacity","B10").',
                'path("capacity",0,"capacity").', 'path("B10",0,"B10").'
            ])

        self.assertEqual(
            parse_coom(
                'behavior {require count(carrier.bags) + count(frame.bags) <= 4}'
            ), [
                'behavior((":root",0)).',
                'require((":root",0),"count(carrier.bags)+count(frame.bags)<=4").',
                'binary(":root","count(carrier.bags)+count(frame.bags)<=4","count(carrier.bags)+count(frame.bags)","<=","4").',
                'binary(":root","count(carrier.bags)+count(frame.bags)","count(carrier.bags)","+","count(frame.bags)").',
                'function(":root","count(carrier.bags)","count","carrier.bags").',
                'path("carrier.bags",0,"carrier").',
                'path("carrier.bags",1,"bags").',
                'function(":root","count(frame.bags)","count","frame.bags").',
                'path("frame.bags",0,"frame").', 'path("frame.bags",1,"bags").'
            ])

        self.assertEqual(
            parse_coom(
                'behavior{imply totalWeight = frontWheel.weight + rearWheel.weight+ sum(carrier.bags.capacity.weight)}'
            ), [
                'behavior((":root",0)).',
                'imply((":root",0),"totalWeight","frontWheel.weight+rearWheel.weight+sum(carrier.bags.capacity.weight)").',
                'path("totalWeight",0,"totalWeight").',
                'binary(":root","frontWheel.weight+rearWheel.weight+sum(carrier.bags.capacity.weight)","frontWheel.weight","+","rearWheel.weight+sum(carrier.bags.capacity.weight)").',
                'binary(":root","rearWheel.weight+sum(carrier.bags.capacity.weight)","rearWheel.weight","+","sum(carrier.bags.capacity.weight)").',
                'path("frontWheel.weight",0,"frontWheel").',
                'path("frontWheel.weight",1,"weight").',
                'path("rearWheel.weight",0,"rearWheel").',
                'path("rearWheel.weight",1,"weight").',
                'function(":root","sum(carrier.bags.capacity.weight)","sum","carrier.bags.capacity.weight").',
                'path("carrier.bags.capacity.weight",0,"carrier").',
                'path("carrier.bags.capacity.weight",1,"bags").',
                'path("carrier.bags.capacity.weight",2,"capacity").',
                'path("carrier.bags.capacity.weight",3,"weight").'
            ])

        self.assertEqual(parse_coom('behavior{readonly totalWeight}'), [])

        # TODO: Test Define statement (needs to be implemented)

    def test_condition(self):
        self.assertEqual(parse_coom('behavior{require a = b || a = c}'), [
            'behavior((":root",0)).', 'require((":root",0),"a=b||a=c").',
            'binary(":root","a=b||a=c","a=b","||","a=c").',
            'binary(":root","a=b","a","=","b").', 'path("a",0,"a").',
            'path("b",0,"b").', 'binary(":root","a=c","a","=","c").',
            'path("a",0,"a").', 'path("c",0,"c").'
        ])

        self.assertEqual(
            parse_coom('behavior{require a = b || a = c || a = d}'), [
                'behavior((":root",0)).',
                'require((":root",0),"a=b||a=c||a=d").',
                'binary(":root","a=b||a=c||a=d","a=b","||","a=c||a=d").',
                'binary(":root","a=c||a=d","a=c","||","a=d").',
                'binary(":root","a=b","a","=","b").', 'path("a",0,"a").',
                'path("b",0,"b").', 'binary(":root","a=c","a","=","c").',
                'path("a",0,"a").', 'path("c",0,"c").',
                'binary(":root","a=d","a","=","d").', 'path("a",0,"a").',
                'path("d",0,"d").'
            ])

        self.assertEqual(parse_coom('behavior{require a = b && a = c}'), [
            'behavior((":root",0)).', 'require((":root",0),"a=b&&a=c").',
            'binary(":root","a=b&&a=c","a=b","&&","a=c").',
            'binary(":root","a=b","a","=","b").', 'path("a",0,"a").',
            'path("b",0,"b").', 'binary(":root","a=c","a","=","c").',
            'path("a",0,"a").', 'path("c",0,"c").'
        ])

        self.assertEqual(
            parse_coom('behavior{require a = b && a = c && a = d}'), [
                'behavior((":root",0)).',
                'require((":root",0),"a=b&&a=c&&a=d").',
                'binary(":root","a=b&&a=c&&a=d","a=b","&&","a=c&&a=d").',
                'binary(":root","a=c&&a=d","a=c","&&","a=d").',
                'binary(":root","a=b","a","=","b").', 'path("a",0,"a").',
                'path("b",0,"b").', 'binary(":root","a=c","a","=","c").',
                'path("a",0,"a").', 'path("c",0,"c").',
                'binary(":root","a=d","a","=","d").', 'path("a",0,"a").',
                'path("d",0,"d").'
            ])

        self.assertEqual(parse_coom('behavior{require ! a = b }'), [
            'behavior((":root",0)).', 'require((":root",0),"!a=b").',
            'unary(":root","!a=b","!","a=b").',
            'binary(":root","a=b","a","=","b").', 'path("a",0,"a").',
            'path("b",0,"b").'
        ])

        self.assertEqual(parse_coom('behavior{require (a = b) }'), [
            'behavior((":root",0)).', 'require((":root",0),"(a=b)").',
            'unary(":root","(a=b)","()","a=b").',
            'binary(":root","a=b","a","=","b").', 'path("a",0,"a").',
            'path("b",0,"b").'
        ])

    def test_formula(self):
        pass


if __name__ == '__main__':
    unittest.main()
