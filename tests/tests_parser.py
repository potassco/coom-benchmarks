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
            parse_coom('behavior {condition a = b require c > 5}'), [
                'behavior((":root",0)).', 'condition((":root",0),"a=b").',
                'binary(":root","a=b","a","=","b").', 'path("a",0,"a").',
                'path("b",0,"b").', 'require((":root",0),"c>5").',
                'binary(":root","c>5","c",">","5").', 'path("c",0,"c").'
            ])

        self.assertEqual(
            parse_coom('behavior {condition a = b default c = d}'), [
                'behavior((":root",0)).', 'condition((":root",0),"a=b").',
                'binary(":root","a=b","a","=","b").', 'path("a",0,"a").',
                'path("b",0,"b").', 'default((":root",0),"c","d").',
                'path("c",0,"c").', 'path("d",0,"d").'
            ])

        self.assertEqual(parse_coom('behavior{imply a = b}'), [
            'behavior((":root",0)).', 'imply((":root",0),"a","b").',
            'path("a",0,"a").', 'path("b",0,"b").'
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
        self.assertEqual(parse_coom('behavior{require a = b + c}'), [
            'behavior((":root",0)).', 'require((":root",0),"a=b+c").',
            'binary(":root","a=b+c","a","=","b+c").', 'path("a",0,"a").',
            'binary(":root","b+c","b","+","c").', 'path("b",0,"b").',
            'path("c",0,"c").'
        ])

        self.assertEqual(parse_coom('behavior{require a = b - c}'), [
            'behavior((":root",0)).', 'require((":root",0),"a=b-c").',
            'binary(":root","a=b-c","a","=","b-c").', 'path("a",0,"a").',
            'binary(":root","b-c","b","-","c").', 'path("b",0,"b").',
            'path("c",0,"c").'
        ])

        self.assertEqual(parse_coom('behavior{require a = b * c}'), [
            'behavior((":root",0)).', 'require((":root",0),"a=b*c").',
            'binary(":root","a=b*c","a","=","b*c").', 'path("a",0,"a").',
            'binary(":root","b*c","b","*","c").', 'path("b",0,"b").',
            'path("c",0,"c").'
        ])
        self.assertEqual(parse_coom('behavior{require a = b / c}'), [
            'behavior((":root",0)).', 'require((":root",0),"a=b/c").',
            'binary(":root","a=b/c","a","=","b/c").', 'path("a",0,"a").',
            'binary(":root","b/c","b","/","c").', 'path("b",0,"b").',
            'path("c",0,"c").'
        ])

        self.assertEqual(parse_coom('behavior{require a = b ^ c}'), [
            'behavior((":root",0)).', 'require((":root",0),"a=b^c").',
            'binary(":root","a=b^c","a","=","b^c").', 'path("a",0,"a").',
            'binary(":root","b^c","b","^","c").', 'path("b",0,"b").',
            'path("c",0,"c").'
        ])

        self.assertEqual(parse_coom('behavior{require a = - b}'), [
            'behavior((":root",0)).', 'require((":root",0),"a=-b").',
            'binary(":root","a=-b","a","=","-b").', 'path("a",0,"a").',
            'unary(":root","-b","-","b").', 'path("b",0,"b").'
        ])

        self.assertEqual(parse_coom('behavior{require a = (b)}'), [
            'behavior((":root",0)).', 'require((":root",0),"a=(b)").',
            'binary(":root","a=(b)","a","=","(b)").', 'path("a",0,"a").',
            'unary(":root","(b)","()","b").', 'path("b",0,"b").'
        ])

        self.assertEqual(parse_coom('behavior{require a = sum(b)}'), [
            'behavior((":root",0)).', 'require((":root",0),"a=sum(b)").',
            'binary(":root","a=sum(b)","a","=","sum(b)").', 'path("a",0,"a").',
            'function(":root","sum(b)","sum","b").', 'path("b",0,"b").'
        ])

        self.assertEqual(parse_coom('behavior{require a = sum(b,c)}'), [
            'behavior((":root",0)).', 'require((":root",0),"a=sum(b,c)").',
            'binary(":root","a=sum(b,c)","a","=","sum(b,c)").',
            'path("a",0,"a").', 'function(":root","sum(b,c)","sum","b").',
            'function(":root","sum(b,c)","sum","c").', 'path("b",0,"b").',
            'path("c",0,"c").'
        ])

        self.assertEqual(parse_coom('behavior{require a = count(b)}'), [
            'behavior((":root",0)).', 'require((":root",0),"a=count(b)").',
            'binary(":root","a=count(b)","a","=","count(b)").',
            'path("a",0,"a").', 'function(":root","count(b)","count","b").',
            'path("b",0,"b").'
        ])

        self.assertEqual(parse_coom('behavior{require a = count(b,c)}'), [
            'behavior((":root",0)).', 'require((":root",0),"a=count(b,c)").',
            'binary(":root","a=count(b,c)","a","=","count(b,c)").',
            'path("a",0,"a").', 'function(":root","count(b,c)","count","b").',
            'function(":root","count(b,c)","count","c").', 'path("b",0,"b").',
            'path("c",0,"c").'
        ])
        self.assertEqual(parse_coom('behavior{require a = min(b)}'), [
            'behavior((":root",0)).', 'require((":root",0),"a=min(b)").',
            'binary(":root","a=min(b)","a","=","min(b)").', 'path("a",0,"a").',
            'function(":root","min(b)","min","b").', 'path("b",0,"b").'
        ])

        self.assertEqual(parse_coom('behavior{require a = min(b,c)}'), [
            'behavior((":root",0)).', 'require((":root",0),"a=min(b,c)").',
            'binary(":root","a=min(b,c)","a","=","min(b,c)").',
            'path("a",0,"a").', 'function(":root","min(b,c)","min","b").',
            'function(":root","min(b,c)","min","c").', 'path("b",0,"b").',
            'path("c",0,"c").'
        ])

        self.assertEqual(parse_coom('behavior{require a = max(b)}'), [
            'behavior((":root",0)).', 'require((":root",0),"a=max(b)").',
            'binary(":root","a=max(b)","a","=","max(b)").', 'path("a",0,"a").',
            'function(":root","max(b)","max","b").', 'path("b",0,"b").'
        ])

        self.assertEqual(parse_coom('behavior{require a = max(b,c)}'), [
            'behavior((":root",0)).', 'require((":root",0),"a=max(b,c)").',
            'binary(":root","a=max(b,c)","a","=","max(b,c)").',
            'path("a",0,"a").', 'function(":root","max(b,c)","max","b").',
            'function(":root","max(b,c)","max","c").', 'path("b",0,"b").',
            'path("c",0,"c").'
        ])

        self.assertEqual(parse_coom('behavior{require a = delta(b)}'), [
            'behavior((":root",0)).', 'require((":root",0),"a=delta(b)").',
            'binary(":root","a=delta(b)","a","=","delta(b)").',
            'path("a",0,"a").', 'function(":root","delta(b)","delta","b").',
            'path("b",0,"b").'
        ])

        self.assertEqual(parse_coom('behavior{require a = delta(b,c)}'), [
            'behavior((":root",0)).', 'require((":root",0),"a=delta(b,c)").',
            'binary(":root","a=delta(b,c)","a","=","delta(b,c)").',
            'path("a",0,"a").', 'function(":root","delta(b,c)","delta","b").',
            'function(":root","delta(b,c)","delta","c").', 'path("b",0,"b").',
            'path("c",0,"c").'
        ])

    def test_path(self):
        self.assertEqual(parse_coom('behavior{require a = b.c.d.e.f}'), [
            'behavior((":root",0)).', 'require((":root",0),"a=b.c.d.e.f").',
            'binary(":root","a=b.c.d.e.f","a","=","b.c.d.e.f").',
            'path("a",0,"a").', 'path("b.c.d.e.f",0,"b").',
            'path("b.c.d.e.f",1,"c").', 'path("b.c.d.e.f",2,"d").',
            'path("b.c.d.e.f",3,"e").', 'path("b.c.d.e.f",4,"f").'
        ])


if __name__ == '__main__':
    unittest.main()
