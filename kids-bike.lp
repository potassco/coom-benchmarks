% product.
% structure(":root",Clothing,)
feature(":root",color,color).
feature(":root",bool,wheelSupport).
feature(":root",wheel,frontWheel).
feature(":root",wheel,rearWheel).


enumeration(bool).
domain(bool,(true;false)).

enumeration(color).
domain(color,(red;green;yellow;blue)).

enumeration(wheel).
attribute(wheel,size).
domain(wheel,(w14;w16;w18;w20)).
value(wheel,w14,size,14).
value(wheel,w16,size,16).
value(wheel,w18,size,18).
value(wheel,w20,size,20).

