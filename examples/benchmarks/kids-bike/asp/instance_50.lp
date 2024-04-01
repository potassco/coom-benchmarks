structure(":root").
feature(":root",color,"Color",1,1).
feature(":root",wheelSupport,"bool",1,1).
feature(":root",frontWheel,"Wheel",1,1).
feature(":root",rearWheel,"Wheel",1,1).

enumeration("Color").
option("Color", "Color1").
option("Color", "Color2").
option("Color", "Color3").
option("Color", "Color4").
option("Color", "Color5").
option("Color", "Color6").
option("Color", "Color7").
option("Color", "Color8").
option("Color", "Color9").
option("Color", "Color10").
option("Color", "Color11").
option("Color", "Color12").
option("Color", "Color13").
option("Color", "Color14").
option("Color", "Color15").
option("Color", "Color16").
option("Color", "Color17").
option("Color", "Color18").
option("Color", "Color19").
option("Color", "Color20").
option("Color", "Color21").
option("Color", "Color22").
option("Color", "Color23").
option("Color", "Color24").
option("Color", "Color25").
option("Color", "Color26").
option("Color", "Color27").
option("Color", "Color28").
option("Color", "Color29").
option("Color", "Color30").
option("Color", "Color31").
option("Color", "Color32").
option("Color", "Color33").
option("Color", "Color34").
option("Color", "Color35").
option("Color", "Color36").
option("Color", "Color37").
option("Color", "Color38").
option("Color", "Color39").
option("Color", "Color40").
option("Color", "Color41").
option("Color", "Color42").
option("Color", "Color43").
option("Color", "Color44").
option("Color", "Color45").
option("Color", "Color46").
option("Color", "Color47").
option("Color", "Color48").
option("Color", "Color49").
option("Color", "Color50").

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
combinations((":root",0),0,"wheelSupport").
combinations((":root",0),1,"rearWheel").
path("wheelSupport",0,wheelSupport).
path("rearWheel",0,rearWheel).
allow((":root",0),(0,0),"True").
allow((":root",0),(1,0),"W14").
allow((":root",0),(1,0),"W16").
allow((":root",0),(0,1),"False").
allow((":root",0),(1,1),"W18").
allow((":root",0),(1,1),"W20").

behavior((":root",1)).
require((":root",1),"frontWheel.size=rearWheel.size").
binary(":root","frontWheel.size=rearWheel.size","frontWheel.size","=","rearWheel.size").
path("frontWheel.size",0,frontWheel).
path("frontWheel.size",1,size).
path("rearWheel.size",0,rearWheel).
path("rearWheel.size",1,size).
