structure(":root").
feature(":root",bikes,"Bike",1,1).

structure("Bike").
feature("Bike",frontWheel,"Wheel",1,1).
feature("Bike",rearWheel,"Wheel",1,1).
feature("Bike",carrier,"Carrier",1,1).
feature("Bike",color,"Color",1,1).

structure("Carrier").
feature("Carrier",bags,"Bag",0,2).

structure("Frame").
feature("Frame",bags,"Bag",0,1).

structure("Bag").
feature("Bag",capacity,"Capacity",1,1).
feature("Bag",material,"Material",1,1).

enumeration("Capacity").
attribute("Capacity",volume,"num").
option("Capacity", "B10").
attr_value("Capacity","B10",volume,10).
option("Capacity", "B20").
attr_value("Capacity","B20",volume,20).
option("Capacity", "B50").
attr_value("Capacity","B50",volume,50).

enumeration("Material").
option("Material", "Cotton").
option("Material", "Leather").
option("Material", "Polyester").

enumeration("Wheel").
attribute("Wheel",size,"num").
option("Wheel", "W25").
attr_value("Wheel","W25",size,25).
option("Wheel", "W26").
attr_value("Wheel","W26",size,26).
option("Wheel", "W27").
attr_value("Wheel","W27",size,27).
option("Wheel", "W28").
attr_value("Wheel","W28",size,28).

enumeration("Color").
option("Color", "Red").
option("Color", "Silver").
option("Color", "Blue").

behavior(("Bike",0)).
require(("Bike",0),"frontWheel.size=rearWheel.size").
binary("Bike","frontWheel.size=rearWheel.size","frontWheel.size","=","rearWheel.size").
path("frontWheel.size",0,frontWheel).
path("frontWheel.size",1,size).
path("rearWheel.size",0,rearWheel).
path("rearWheel.size",1,size).

behavior(("Bike",1)).
condition(("Bike",1),"color=Red").
binary("Bike","color=Red","color","=","Red").
path("color",0,color).
constant("Red").
require(("Bike",1),"frontWheel.size=25").
binary("Bike","frontWheel.size=25","frontWheel.size","=","25").
path("frontWheel.size",0,frontWheel).
path("frontWheel.size",1,size).
number("25",25).

behavior(("Bag",2)).
condition(("Bag",2),"material=Leather").
binary("Bag","material=Leather","material","=","Leather").
path("material",0,material).
constant("Leather").
require(("Bag",2),"capacity=B10").
binary("Bag","capacity=B10","capacity","=","B10").
path("capacity",0,capacity).
constant("B10").
