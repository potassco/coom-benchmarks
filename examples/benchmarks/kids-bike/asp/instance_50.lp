structure(":root").
feature(":root",color,"Color",1,1).
feature(":root",wheelSupport,"bool",1,1).
feature(":root",basket,"Position",1,1).
feature(":root",basketColor,"Color",1,1).
feature(":root",frontWheel,"Wheel",1,1).
feature(":root",rearWheel,"Wheel",1,1).

enumeration("Color").
option("Color", "Red").
option("Color", "Green").
option("Color", "Blue").
option("Color", "Silver").
option("Color", "Black").
option("Color", "Yellow").
option("Color", "Purple").
option("Color", "Gray").
option("Color", "Orange").
option("Color", "White").

enumeration("Position").
option("Position", "Front").
option("Position", "Rear").

enumeration("Wheel").
attribute("Wheel",size,"num").
option("Wheel", "W14").
attr_value("Wheel","W14",size,14).
option("Wheel", "W15").
attr_value("Wheel","W15",size,15).
option("Wheel", "W16").
attr_value("Wheel","W16",size,16).
option("Wheel", "W17").
attr_value("Wheel","W17",size,17).
option("Wheel", "W18").
attr_value("Wheel","W18",size,18).
option("Wheel", "W19").
attr_value("Wheel","W19",size,19).
option("Wheel", "W20").
attr_value("Wheel","W20",size,20).

behavior((":root",0)).
condition((":root",0),"color=Yellow").
binary(":root","color=Yellow","color","=","Yellow").
path("color",0,color).
constant("Yellow").
require((":root",0),"frontWheel.size>16").
binary(":root","frontWheel.size>16","frontWheel.size",">","16").
path("frontWheel.size",0,frontWheel).
path("frontWheel.size",1,size).
number("16",16).

behavior((":root",1)).
combinations((":root",1),0,"wheelSupport").
combinations((":root",1),1,"rearWheel").
path("wheelSupport",0,wheelSupport).
path("rearWheel",0,rearWheel).
allow((":root",1),(0,0),"True").
allow((":root",1),(1,0),"W14").
allow((":root",1),(1,0),"W15").
allow((":root",1),(1,0),"W16").
allow((":root",1),(1,0),"W17").
allow((":root",1),(0,1),"False").
allow((":root",1),(1,1),"W18").
allow((":root",1),(1,1),"W19").
allow((":root",1),(1,1),"W20").

behavior((":root",2)).
require((":root",2),"frontWheel.size=rearWheel.size").
binary(":root","frontWheel.size=rearWheel.size","frontWheel.size","=","rearWheel.size").
path("frontWheel.size",0,frontWheel).
path("frontWheel.size",1,size).
path("rearWheel.size",0,rearWheel).
path("rearWheel.size",1,size).

behavior((":root",3)).
require((":root",3),"basketColor!=Purple").
binary(":root","basketColor!=Purple","basketColor","!=","Purple").
path("basketColor",0,basketColor).
constant("Purple").

behavior((":root",4)).
require((":root",4),"color!=White").
binary(":root","color!=White","color","!=","White").
path("color",0,color).
constant("White").

behavior((":root",5)).
condition((":root",5),"color=Green").
binary(":root","color=Green","color","=","Green").
path("color",0,color).
constant("Green").
require((":root",5),"basketColor=Yellow").
binary(":root","basketColor=Yellow","basketColor","=","Yellow").
path("basketColor",0,basketColor).
constant("Yellow").

behavior((":root",6)).
combinations((":root",6),0,"basket").
combinations((":root",6),1,"basketColor").
path("basket",0,basket).
path("basketColor",0,basketColor).
allow((":root",6),(0,0),"Front").
allow((":root",6),(1,0),"Red").
allow((":root",6),(1,0),"Green").
allow((":root",6),(1,0),"Blue").
allow((":root",6),(1,0),"Silver").
allow((":root",6),(1,0),"Black").
allow((":root",6),(1,0),"Gray").
allow((":root",6),(1,0),"White").
allow((":root",6),(0,1),"Rear").
allow((":root",6),(1,1),"Red").
allow((":root",6),(1,1),"Green").
allow((":root",6),(1,1),"Blue").
allow((":root",6),(1,1),"Silver").
allow((":root",6),(1,1),"Black").
allow((":root",6),(1,1),"Yellow").
allow((":root",6),(1,1),"Orange").
