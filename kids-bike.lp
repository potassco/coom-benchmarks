feature(":root",color,color).
feature(":root",bool,wheelSupport).
feature(":root",wheel,frontWheel).
feature(":root",wheel,rearWheel).


enumeration(bool).
option(bool,(true;false)).

enumeration(color).
option(color,(red;green;yellow;blue)).

enumeration(wheel).
attribute(wheel,size).
option(wheel,(w14;w16;w18;w20)).
value(wheel,w14,size,14).
value(wheel,w16,size,16).
value(wheel,w18,size,18).
value(wheel,w20,size,20).


%%% Constraints
behavior(":root",0,"requires").
condition(":root",0,formula1).
formula(formula1,).
% path(0,0,frontWheel). path(0,1,size).
require(":root",0,(size,(frontWheel,())),">",16).


behavior(":root",1,"combination").
header(":root",1,0,path1).
path(path1,0,wheelSupport).
header(":root",1,1,path2).
path(path2,0,rearWheel).
allow(":root",1,(0,0),true).
allow(":root",1,(1,0),(w14;w16)).
allow(":root",1,(0,1),false).
allow(":root",1,(1,2),(w18;w20)).


behiavior(":root",2,"requires").
require(":root",2,(size,(frontWheel,())),"==",(size,(rearWheel,()))).

