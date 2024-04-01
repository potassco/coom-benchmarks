structure(":root").
feature(":root",totalPrice,"num",1,1).
range(":root",totalPrice,0,20000).
feature(":root",maxPrice,"num",1,1).
range(":root",maxPrice,0,20000).
feature(":root",bikes,"Bike",1,2).

structure("Bike").
feature("Bike",totalWeight,"num",1,1).
range("Bike",totalWeight,1,10000).
feature("Bike",maxWeight,"num",1,1).
range("Bike",maxWeight,1,10).
feature("Bike",totalVolume,"num",1,1).
range("Bike",totalVolume,0,200).
feature("Bike",requestedVolume,"num",1,1).
range("Bike",requestedVolume,0,200).
feature("Bike",price,"num",1,1).
range("Bike",price,0,2000).
feature("Bike",frontWheel,"Wheel",1,1).
feature("Bike",rearWheel,"Wheel",1,1).
feature("Bike",frame,"Frame",1,1).
feature("Bike",carrier,"Carrier",1,1).
feature("Bike",color,"Color",1,1).

structure("Carrier").
feature("Carrier",bags,"Bag",0,3).

structure("Frame").
feature("Frame",bags,"Bag",0,2).

structure("Bag").
feature("Bag",material,"Material",1,1).
feature("Bag",price,"num",1,1).
range("Bag",price,0,200).

enumeration("Capacity").
attribute("Capacity",volume,"num").
attribute("Capacity",weight,"num").
attribute("Capacity",price,"num").
option("Capacity", "B10").
attr_value("Capacity","B10",volume,10).
attr_value("Capacity","B10",weight,100).
attr_value("Capacity","B10",price,20).
option("Capacity", "B20").
attr_value("Capacity","B20",volume,20).
attr_value("Capacity","B20",weight,250).
attr_value("Capacity","B20",price,40).
option("Capacity", "B50").
attr_value("Capacity","B50",volume,50).
attr_value("Capacity","B50",weight,600).
attr_value("Capacity","B50",price,75).
option("Capacity", "B100").
attr_value("Capacity","B100",volume,100).
attr_value("Capacity","B100",weight,1200).
attr_value("Capacity","B100",price,130).

enumeration("Material").
attribute("Material",price,"num").
option("Material", "Cotton").
attr_value("Material","Cotton",price,15).
option("Material", "Leather").
attr_value("Material","Leather",price,50).
option("Material", "Polyester").
attr_value("Material","Polyester",price,0).

enumeration("Wheel").
attribute("Wheel",size,"num").
attribute("Wheel",weight,"num").
attribute("Wheel",price,"num").
option("Wheel", "W20").
attr_value("Wheel","W20",size,20).
attr_value("Wheel","W20",weight,650).
attr_value("Wheel","W20",price,50).
option("Wheel", "W22").
attr_value("Wheel","W22",size,22).
attr_value("Wheel","W22",weight,700).
attr_value("Wheel","W22",price,60).
option("Wheel", "W24").
attr_value("Wheel","W24",size,24).
attr_value("Wheel","W24",weight,800).
attr_value("Wheel","W24",price,75).
option("Wheel", "W26").
attr_value("Wheel","W26",size,26).
attr_value("Wheel","W26",weight,900).
attr_value("Wheel","W26",price,95).
option("Wheel", "W28").
attr_value("Wheel","W28",size,28).
attr_value("Wheel","W28",weight,1000).
attr_value("Wheel","W28",price,120).

enumeration("Color").
option("Color", "Red").
option("Color", "Green").
option("Color", "Yellow").
option("Color", "Blue").

behavior((":root",0)).
imply((":root",0),totalPrice,"sum(bikes.price)").
path("totalPrice",0,totalPrice).
function(":root","sum(bikes.price)","sum","bikes.price").
path("bikes.price",0,bikes).
path("bikes.price",1,price).

behavior((":root",1)).
require((":root",1),"totalPrice<=maxPrice").
binary(":root","totalPrice<=maxPrice","totalPrice","<=","maxPrice").
path("totalPrice",0,totalPrice).
path("maxPrice",0,maxPrice).

behavior(("Bike",2)).
require(("Bike",2),"count(carrier.bags)+count(frame.bags)<=4").
binary("Bike","count(carrier.bags)+count(frame.bags)<=4","count(carrier.bags)+count(frame.bags)","<=","4").
binary("Bike","count(carrier.bags)+count(frame.bags)","count(carrier.bags)","+","count(frame.bags)").
function("Bike","count(carrier.bags)","count","carrier.bags").
path("carrier.bags",0,carrier).
path("carrier.bags",1,bags).
function("Bike","count(frame.bags)","count","frame.bags").
path("frame.bags",0,frame).
path("frame.bags",1,bags).
number("4",4).

behavior(("Bike",3)).
require(("Bike",3),"frontWheel.size<=rearWheel.size").
binary("Bike","frontWheel.size<=rearWheel.size","frontWheel.size","<=","rearWheel.size").
path("frontWheel.size",0,frontWheel).
path("frontWheel.size",1,size).
path("rearWheel.size",0,rearWheel).
path("rearWheel.size",1,size).

behavior(("Bike",4)).
imply(("Bike",4),totalWeight,"frontWheel.weight+rearWheel.weight+sum(carrier.bags.capacity.weight)+sum(frame.bags.capacity.weight)").
path("totalWeight",0,totalWeight).
binary("Bike","frontWheel.weight+rearWheel.weight+sum(carrier.bags.capacity.weight)+sum(frame.bags.capacity.weight)","frontWheel.weight","+","rearWheel.weight+sum(carrier.bags.capacity.weight)+sum(frame.bags.capacity.weight)").
binary("Bike","rearWheel.weight+sum(carrier.bags.capacity.weight)+sum(frame.bags.capacity.weight)","rearWheel.weight","+","sum(carrier.bags.capacity.weight)+sum(frame.bags.capacity.weight)").
binary("Bike","sum(carrier.bags.capacity.weight)+sum(frame.bags.capacity.weight)","sum(carrier.bags.capacity.weight)","+","sum(frame.bags.capacity.weight)").
path("frontWheel.weight",0,frontWheel).
path("frontWheel.weight",1,weight).
path("rearWheel.weight",0,rearWheel).
path("rearWheel.weight",1,weight).
function("Bike","sum(carrier.bags.capacity.weight)","sum","carrier.bags.capacity.weight").
path("carrier.bags.capacity.weight",0,carrier).
path("carrier.bags.capacity.weight",1,bags).
path("carrier.bags.capacity.weight",2,capacity).
path("carrier.bags.capacity.weight",3,weight).
function("Bike","sum(frame.bags.capacity.weight)","sum","frame.bags.capacity.weight").
path("frame.bags.capacity.weight",0,frame).
path("frame.bags.capacity.weight",1,bags).
path("frame.bags.capacity.weight",2,capacity).
path("frame.bags.capacity.weight",3,weight).

behavior(("Bike",5)).
require(("Bike",5),"totalWeight<=maxWeight*1000").
binary("Bike","totalWeight<=maxWeight*1000","totalWeight","<=","maxWeight*1000").
path("totalWeight",0,totalWeight).
binary("Bike","maxWeight*1000","maxWeight","*","1000").
path("maxWeight",0,maxWeight).
number("1000",1000).

behavior(("Bike",6)).
imply(("Bike",6),totalVolume,"sum(carrier.bags.capacity.volume)+sum(frame.bags.capacity.volume)").
path("totalVolume",0,totalVolume).
binary("Bike","sum(carrier.bags.capacity.volume)+sum(frame.bags.capacity.volume)","sum(carrier.bags.capacity.volume)","+","sum(frame.bags.capacity.volume)").
function("Bike","sum(carrier.bags.capacity.volume)","sum","carrier.bags.capacity.volume").
path("carrier.bags.capacity.volume",0,carrier).
path("carrier.bags.capacity.volume",1,bags).
path("carrier.bags.capacity.volume",2,capacity).
path("carrier.bags.capacity.volume",3,volume).
function("Bike","sum(frame.bags.capacity.volume)","sum","frame.bags.capacity.volume").
path("frame.bags.capacity.volume",0,frame).
path("frame.bags.capacity.volume",1,bags).
path("frame.bags.capacity.volume",2,capacity).
path("frame.bags.capacity.volume",3,volume).

behavior(("Bike",7)).
require(("Bike",7),"totalVolume>=requestedVolume").
binary("Bike","totalVolume>=requestedVolume","totalVolume",">=","requestedVolume").
path("totalVolume",0,totalVolume).
path("requestedVolume",0,requestedVolume).

behavior(("Bike",8)).
imply(("Bike",8),price,"frontWheel.price+rearWheel.price+sum(carrier.bags.price)+sum(frame.bags.price)").
path("price",0,price).
binary("Bike","frontWheel.price+rearWheel.price+sum(carrier.bags.price)+sum(frame.bags.price)","frontWheel.price","+","rearWheel.price+sum(carrier.bags.price)+sum(frame.bags.price)").
binary("Bike","rearWheel.price+sum(carrier.bags.price)+sum(frame.bags.price)","rearWheel.price","+","sum(carrier.bags.price)+sum(frame.bags.price)").
binary("Bike","sum(carrier.bags.price)+sum(frame.bags.price)","sum(carrier.bags.price)","+","sum(frame.bags.price)").
path("frontWheel.price",0,frontWheel).
path("frontWheel.price",1,price).
path("rearWheel.price",0,rearWheel).
path("rearWheel.price",1,price).
function("Bike","sum(carrier.bags.price)","sum","carrier.bags.price").
path("carrier.bags.price",0,carrier).
path("carrier.bags.price",1,bags).
path("carrier.bags.price",2,price).
function("Bike","sum(frame.bags.price)","sum","frame.bags.price").
path("frame.bags.price",0,frame).
path("frame.bags.price",1,bags).
path("frame.bags.price",2,price).

behavior(("Bike",9)).
condition(("Bike",9),"color=Red").
binary("Bike","color=Red","color","=","Red").
path("color",0,color).
constant("Red").
require(("Bike",9),"frontWheel.size=20").
binary("Bike","frontWheel.size=20","frontWheel.size","=","20").
path("frontWheel.size",0,frontWheel).
path("frontWheel.size",1,size).
number("20",20).

behavior(("Bag",10)).
imply(("Bag",10),price,"capacity.price+material.price").
path("price",0,price).
binary("Bag","capacity.price+material.price","capacity.price","+","material.price").
path("capacity.price",0,capacity).
path("capacity.price",1,price).
path("material.price",0,material).
path("material.price",1,price).

behavior(("Bag",11)).
condition(("Bag",11),"material=Leather").
binary("Bag","material=Leather","material","=","Leather").
path("material",0,material).
constant("Leather").
require(("Bag",11),"capacity=B10").
binary("Bag","capacity=B10","capacity","=","B10").
path("capacity",0,capacity).
constant("B10").
