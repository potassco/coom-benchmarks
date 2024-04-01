structure(":root").
feature(":root",saddle,"Saddle",1,1).
feature(":root",bag,"Bag",1,1).

enumeration("Saddle").
option("Saddle", "Standard").
option("Saddle", "Comfort").
option("Saddle", "Vintage").

structure("Bag").
feature("Bag",material,"Material",1,1).

enumeration("Material").
option("Material", "Leather").
option("Material", "Polyester").

behavior((":root",0)).
combinations((":root",0),0,"saddle").
combinations((":root",0),1,"bag.material").
path("saddle",0,saddle).
path("bag.material",0,bag).
path("bag.material",1,material).
allow((":root",0),(0,0),"Standard").
allow((":root",0),(1,0),"Polyester").
allow((":root",0),(0,1),"Vintage").
allow((":root",0),(1,1),"Leather").
