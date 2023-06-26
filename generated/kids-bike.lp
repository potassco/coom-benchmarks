structure(":root").
feature(":root", "color", 1, 1).
feature(":root", "wheelSupport", 1, 1).
feature(":root", "frontWheel", 1, 1).
feature(":root", "rearWheel", 1, 1).
enumeration("Color").
option("Color", "Red").
option("Color", "Green").
option("Color", "Yellow").
option("Color", "Blue").
enumeration("Wheel").
attribute("Wheel","size").
option("Wheel", "W14").
value("Wheel","W14","size",14).
option("Wheel", "W16").
value("Wheel","W16","size",16).
option("Wheel", "W18").
value("Wheel","W18","size",18).
option("Wheel", "W20").
value("Wheel","W20","size",20).

behavior((":root",0)).
condition((":root",0),"color=Yellow").
path("color",0,"color").
path("Yellow",0,"Yellow").
require((":root",0),"frontWheel.size>16").
path("frontWheel.size",0,"frontWheel").
path("frontWheel.size",1,"size").

behavior((":root",1)).
combinations((":root",1),0,"wheelSupport").
combinations((":root",1),1,"rearWheel").
path("wheelSupport",0,"wheelSupport").
path("rearWheel",0,"rearWheel").
allow((":root",1),(0,0),"True").
allow((":root",1),(1,0),"W14").
allow((":root",1),(1,0),"W16").
allow((":root",1),(0,1),"False").
allow((":root",1),(1,1),"W18").
allow((":root",1),(1,1),"W20").

behavior((":root",2)).
require((":root",2),"frontWheel.size=rearWheel.size").
path("frontWheel.size",0,"frontWheel").
path("frontWheel.size",1,"size").
path("rearWheel.size",0,"rearWheel").
path("rearWheel.size",1,"size").
