structure(":root").
feature(":root","totalWeight","num",1,1).
range(":root","totalWeight",#inf,#sup).
feature(":root","maxWeight","num",1,1).
range(":root","maxWeight",1,100).
feature(":root","totalVolume","num",1,1).
range(":root","totalVolume",0,200).
feature(":root","requestedVolume","num",1,1).
range(":root","requestedVolume",0,200).
feature(":root","frontWheel","Wheel",1,1).
feature(":root","rearWheel","Wheel",1,1).
feature(":root","frame","Frame",1,1).
feature(":root","carrier","Carrier",1,1).
feature(":root","color","Color",1,1).
structure("Carrier").
feature("Carrier","bags","Bag",0,3).
structure("Frame").
feature("Frame","bags","Bag",0,2).
structure("Bag").
feature("Bag","capacity","Capacity",1,1).
feature("Bag","material","Material",1,1).
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
binary("count(carrier.bags)+count(frame.bags)","count(carrier.bags)","+","count(frame.bags)").
function("count(carrier.bags)","count","carrier.bags").
path("carrier.bags",0,"carrier").
path("carrier.bags",1,"bags").
function("count(frame.bags)","count","frame.bags").
path("frame.bags",0,"frame").
path("frame.bags",1,"bags").

behavior((":root",1)).
imply((":root",1),"totalWeight","frontWheel.weight+rearWheel.weight+sum(carrier.bags.capacity.weight)+sum(frame.bags.capacity.weight)").
path("totalWeight",0,"totalWeight").
binary("frontWheel.weight+rearWheel.weight+sum(carrier.bags.capacity.weight)+sum(frame.bags.capacity.weight)","frontWheel.weight","+","rearWheel.weight+sum(carrier.bags.capacity.weight)+sum(frame.bags.capacity.weight)").
binary("rearWheel.weight+sum(carrier.bags.capacity.weight)+sum(frame.bags.capacity.weight)","rearWheel.weight","+","sum(carrier.bags.capacity.weight)+sum(frame.bags.capacity.weight)").
binary("sum(carrier.bags.capacity.weight)+sum(frame.bags.capacity.weight)","sum(carrier.bags.capacity.weight)","+","sum(frame.bags.capacity.weight)").
path("frontWheel.weight",0,"frontWheel").
path("frontWheel.weight",1,"weight").
path("rearWheel.weight",0,"rearWheel").
path("rearWheel.weight",1,"weight").
function("sum(carrier.bags.capacity.weight)","sum","carrier.bags.capacity.weight").
path("carrier.bags.capacity.weight",0,"carrier").
path("carrier.bags.capacity.weight",1,"bags").
path("carrier.bags.capacity.weight",2,"capacity").
path("carrier.bags.capacity.weight",3,"weight").
function("sum(frame.bags.capacity.weight)","sum","frame.bags.capacity.weight").
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
imply((":root",3),"totalVolume","sum(carrier.bags.capacity.volume)+sum(frame.bags.capacity.volume)").
path("totalVolume",0,"totalVolume").
binary("sum(carrier.bags.capacity.volume)+sum(frame.bags.capacity.volume)","sum(carrier.bags.capacity.volume)","+","sum(frame.bags.capacity.volume)").
function("sum(carrier.bags.capacity.volume)","sum","carrier.bags.capacity.volume").
path("carrier.bags.capacity.volume",0,"carrier").
path("carrier.bags.capacity.volume",1,"bags").
path("carrier.bags.capacity.volume",2,"capacity").
path("carrier.bags.capacity.volume",3,"volume").
function("sum(frame.bags.capacity.volume)","sum","frame.bags.capacity.volume").
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
default((":root",6),"color","Red").
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
default(("Bag",8),"capacity","B10").
path("capacity",0,"capacity").
path("B10",0,"B10").
