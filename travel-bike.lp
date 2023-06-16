feature(":root",num,totalWeight).
feature(":root",num,maxWeight).
range(":root",maxWeight,1000,100000).

feature(":root",totalVolume).
range(":root",totalVolume,0,200).

feature(":root",num,requestedVolume).
range(":root",requestedVolume,0,200).

feature(":root",wheel,frontWheel).
feature(":root",wheel,rearWheel).
feature(":root",frame,frame).
feature(":root",carrier,carrier).
feature(":root",color,color).

structure(carrier).
feature(carrier,bag,bags).
cardinality(carrier,bags,0,3).

structure(frame).
feature(frame,bag,bags).
cardinality(frame,bags,0,2).

structure(bag).
feature(bag,capacity,capacity).
feature(bag,material,material).

enumeration(capacity).
attribute(capacity,volume).
attribute(capacity,weight).
domain(capacity,(b10;b20;b50;b100)).
value(capacity,b10,volume,10).
value(capacity,b10,weight,100).
value(capacity,b20,volume,20).
value(capacity,b20,weight,250).
value(capacity,b50,volume,50).
value(capacity,b50,weight,600).
value(capacity,b100,volume,100).
value(capacity,b100,weight,1200).

enumeration(material).
domain(material,(cotton;leather;polyester)).

enumeration(wheel).
attribute(wheel,size).
attribute(wheel,weight).
domain(wheel,(w20;w22;w24;w26;w28)).
value(wheel,w20,size,20).
value(wheel,w20,weight,650).
value(wheel,w22,size,22).
value(wheel,w22,weight,700).
value(wheel,w24,size,24).
value(wheel,w24,weight,800).
value(wheel,w26,size,26).
value(wheel,w26,weight,900).
value(wheel,w28,size,28).
value(wheel,w28,weight,1000).

%%% Constraints
behavior(":root",0,"requires").
require(":root",0,count((bags,(carrier,())))).
% TODO

behavior(":root",1,"imply").
imply(":root",1,totalWeight).


behavior(bag,0,"default").
condition(bag,0,material,leather).
default(bag,0,capacity,b10).
