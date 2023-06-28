structure(":root").
feature("num", "totalWeight", 1, 1).
feature("num", "maxWeight", 1, 1).
feature("num", "totalVolume", 1, 1).
feature("num", "requestedVolume", 1, 1).
feature(":root", "frontWheel", 1, 1).
feature(":root", "rearWheel", 1, 1).
feature(":root", "frame", 1, 1).
feature(":root", "carrier", 1, 1).
feature(":root", "color", 1, 1).
structure("Carrier").
feature(":root", "bags", [@61,263:263='0',<73>,14:1], [@63,266:266='3',<73>,14:4]).
structure("Frame").
feature(":root", "bags", [@73,307:307='0',<73>,18:1], [@75,310:310='2',<73>,18:4]).
structure("Bag").
feature(":root", "capacity", 1, 1).
feature(":root", "material", 1, 1).
enumeration("Capacity").
attribute("Capacity","volume").
attribute("Capacity","weight").
option("Capacity", "B10").
value("Capacity","B10","volume",10).
value("Capacity","B10","weight",100).
option("Capacity", "B20").
value("Capacity","B20","volume",20).
value("Capacity","B20","weight",250).
option("Capacity", "B50").
value("Capacity","B50","volume",50).
value("Capacity","B50","weight",600).
option("Capacity", "B100").
value("Capacity","B100","volume",100).
value("Capacity","B100","weight",1200).
enumeration("Material").
option("Material", "Cotton").
option("Material", "Leather").
option("Material", "Polyester").
enumeration("Wheel").
attribute("Wheel","size").
attribute("Wheel","weight").
option("Wheel", "W20").
value("Wheel","W20","size",20).
value("Wheel","W20","weight",650).
option("Wheel", "W22").
value("Wheel","W22","size",22).
value("Wheel","W22","weight",700).
option("Wheel", "W24").
value("Wheel","W24","size",24).
value("Wheel","W24","weight",800).
option("Wheel", "W26").
value("Wheel","W26","size",26).
value("Wheel","W26","weight",900).
option("Wheel", "W28").
value("Wheel","W28","size",28).
value("Wheel","W28","weight",1000).

behavior((":root",0)).
require((":root",0),"count(carrier.bags)+count(frame.bags)<=4").
binary("count(carrier.bags)+count(frame.bags)<=4","count(carrier.bags)+count(frame.bags)","<=","4").
path("carrier.bags",0,"carrier").
path("carrier.bags",1,"bags").
path("frame.bags",0,"frame").
path("frame.bags",1,"bags").

behavior((":root",1)).
path("totalWeight",0,"totalWeight").
path("frontWheel.weight",0,"frontWheel").
path("frontWheel.weight",1,"weight").
path("rearWheel.weight",0,"rearWheel").
path("rearWheel.weight",1,"weight").
path("carrier.bags.capacity.weight",0,"carrier").
path("carrier.bags.capacity.weight",1,"bags").
path("carrier.bags.capacity.weight",2,"capacity").
path("carrier.bags.capacity.weight",3,"weight").
path("frame.bags.capacity.weight",0,"frame").
path("frame.bags.capacity.weight",1,"bags").
path("frame.bags.capacity.weight",2,"capacity").
path("frame.bags.capacity.weight",3,"weight").

behavior((":root",2)).
require((":root",2),"totalWeight<=maxWeight").
binary("totalWeight<=maxWeight","totalWeight","<=","maxWeight").
path("totalWeight",0,"totalWeight").
path("maxWeight",0,"maxWeight").

behavior((":root",3)).
path("totalVolume",0,"totalVolume").
path("carrier.bags.capacity.volume",0,"carrier").
path("carrier.bags.capacity.volume",1,"bags").
path("carrier.bags.capacity.volume",2,"capacity").
path("carrier.bags.capacity.volume",3,"volume").
path("frame.bags.capacity.volume",0,"frame").
path("frame.bags.capacity.volume",1,"bags").
path("frame.bags.capacity.volume",2,"capacity").
path("frame.bags.capacity.volume",3,"volume").

behavior((":root",4)).
require((":root",4),"totalVolume>=requestedVolume").
binary("totalVolume>=requestedVolume","totalVolume",">=","requestedVolume").
path("totalVolume",0,"totalVolume").
path("requestedVolume",0,"requestedVolume").

behavior((":root",5)).
path("totalWeight",0,"totalWeight").

behavior((":root",6)).
path("color",0,"color").
path("Red",0,"Red").

behavior((":root",7)).
condition((":root",7),"color=Red").
binary("color=Red","color","=","Red").
path("color",0,"color").
path("Red",0,"Red").
require((":root",7),"frontWheel.size=20").
binary("frontWheel.size=20","frontWheel.size","=","20").
path("frontWheel.size",0,"frontWheel").
path("frontWheel.size",1,"size").

behavior(("Bag",8)).
condition(("Bag",8),"material=Leather").
binary("material=Leather","material","=","Leather").
path("material",0,"material").
path("Leather",0,"Leather").
path("capacity",0,"capacity").
path("B10",0,"B10").
