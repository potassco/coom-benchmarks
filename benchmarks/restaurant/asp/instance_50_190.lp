structure(":root").
feature(":root",bigTables,"BigTable",1,50).
feature(":root",smallTables,"SmallTable",1,50).
feature(":root",totalPlaces,"num",1,500).
range(":root",totalPlaces,#inf,#sup).

structure("BigTable").
feature("BigTable",chairs,"Chair",3,5).

structure("SmallTable").
feature("SmallTable",chairs,"Chair",1,2).

structure("Chair").

behavior((":root",0)).
require((":root",0),"totalPlaces=190").
binary(":root","totalPlaces=190","totalPlaces","=","190").
path("totalPlaces",0,totalPlaces).
number("190",190).

behavior((":root",1)).
imply((":root",1),totalPlaces,"count(bigTables.chairs)+count(smallTables.chairs)").
path("totalPlaces",0,totalPlaces).
binary(":root","count(bigTables.chairs)+count(smallTables.chairs)","count(bigTables.chairs)","+","count(smallTables.chairs)").
function(":root","count(bigTables.chairs)","count","bigTables.chairs").
path("bigTables.chairs",0,bigTables).
path("bigTables.chairs",1,chairs).
function(":root","count(smallTables.chairs)","count","smallTables.chairs").
path("smallTables.chairs",0,smallTables).
path("smallTables.chairs",1,chairs).
