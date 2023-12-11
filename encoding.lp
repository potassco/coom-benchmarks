instance((),":root") :- structure(":root").

variable(Path,Feature,Type) :- instance(Path,Context), feature(Context,Feature,Type,_,_), enumeration(Type).
{  value(Path,Feature,Option) : option(Type,Option) } :- variable(Path,Feature,Type).
:-  {  value(Path,Feature,Option) : option(Type,Option) } != 1, variable(Path,Feature,Type).

% % Derive associated attribute values
value(Path,Type,Option,Attr,V):- variable(Path,Feature,Type), attr_value(Type,Option,Attr,V), value(Path,Feature,Option).





% Always include boolean enumeration
enumeration("bool").
option("bool", "True").
option("bool", "False").

#show instance/2.
#show value/3.
#show value/5.

