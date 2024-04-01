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
option("Color", "Color51").
option("Color", "Color52").
option("Color", "Color53").
option("Color", "Color54").
option("Color", "Color55").
option("Color", "Color56").
option("Color", "Color57").
option("Color", "Color58").
option("Color", "Color59").
option("Color", "Color60").
option("Color", "Color61").
option("Color", "Color62").
option("Color", "Color63").
option("Color", "Color64").
option("Color", "Color65").
option("Color", "Color66").
option("Color", "Color67").
option("Color", "Color68").
option("Color", "Color69").
option("Color", "Color70").
option("Color", "Color71").
option("Color", "Color72").
option("Color", "Color73").
option("Color", "Color74").
option("Color", "Color75").
option("Color", "Color76").
option("Color", "Color77").
option("Color", "Color78").
option("Color", "Color79").
option("Color", "Color80").
option("Color", "Color81").
option("Color", "Color82").
option("Color", "Color83").
option("Color", "Color84").
option("Color", "Color85").
option("Color", "Color86").
option("Color", "Color87").
option("Color", "Color88").
option("Color", "Color89").
option("Color", "Color90").
option("Color", "Color91").
option("Color", "Color92").
option("Color", "Color93").
option("Color", "Color94").
option("Color", "Color95").
option("Color", "Color96").
option("Color", "Color97").
option("Color", "Color98").
option("Color", "Color99").
option("Color", "Color100").
option("Color", "Color101").
option("Color", "Color102").
option("Color", "Color103").
option("Color", "Color104").
option("Color", "Color105").
option("Color", "Color106").
option("Color", "Color107").
option("Color", "Color108").
option("Color", "Color109").
option("Color", "Color110").
option("Color", "Color111").
option("Color", "Color112").
option("Color", "Color113").
option("Color", "Color114").
option("Color", "Color115").
option("Color", "Color116").
option("Color", "Color117").
option("Color", "Color118").
option("Color", "Color119").
option("Color", "Color120").
option("Color", "Color121").
option("Color", "Color122").
option("Color", "Color123").
option("Color", "Color124").
option("Color", "Color125").
option("Color", "Color126").
option("Color", "Color127").
option("Color", "Color128").
option("Color", "Color129").
option("Color", "Color130").
option("Color", "Color131").
option("Color", "Color132").
option("Color", "Color133").
option("Color", "Color134").
option("Color", "Color135").
option("Color", "Color136").
option("Color", "Color137").
option("Color", "Color138").
option("Color", "Color139").
option("Color", "Color140").
option("Color", "Color141").
option("Color", "Color142").
option("Color", "Color143").
option("Color", "Color144").
option("Color", "Color145").
option("Color", "Color146").
option("Color", "Color147").
option("Color", "Color148").
option("Color", "Color149").
option("Color", "Color150").
option("Color", "Color151").
option("Color", "Color152").
option("Color", "Color153").
option("Color", "Color154").
option("Color", "Color155").
option("Color", "Color156").
option("Color", "Color157").
option("Color", "Color158").
option("Color", "Color159").
option("Color", "Color160").

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
