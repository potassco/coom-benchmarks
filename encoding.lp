instance((),":root") :- structure(":root").

% TODO: Incorporate cardinalities
variable(Instance,Feature,Type) :- instance(Instance,Context), feature(Context,Feature,Type,_,_), enumeration(Type).
{  value(Instance,Feature,Option) : option(Type,Option) } :- variable(Instance,Feature,Type).
:-  {  value(Instance,Feature,Option) : option(Type,Option) } != 1, variable(Instance,Feature,Type).

% % Derive associated attribute values
value((Feature,Instance),Attr,V):- variable(Instance,Feature,Type), attr_value(Type,Option,Attr,V), value(Instance,Feature,Option).

%%% Constraints
constraint(Instance,(Context,Idx)) :- behavior((Context,Idx)), instance(Instance,Context).

unsat(Instance, Constraint) :- condition_sat(Instance,Constraint,Condition), not require_sat(Instance,Constraint,_).
condition_sat(Instance,Constraint,Condition) :- constraint(Instance,Constraint), condition(Constraint,Condition), binary_sat(Instance,Constraint,Condition).

binary_values(Instance,Formula,V1,Operator,V2) :- binary(Context,Formula,Path1,Operator,Path2), instance(Instance,Context),
                                                path_value(Instance,Path1,V1),
                                                path_value(Instance,Path2,V2).
binary_sat(Instance,Formula) :- binary_values(Instance,Formula,V1,"=",V2), V1 = V2.
binary_sat(Instance,Formula) :- binary_values(Instance,Formula,V1,"!=",V2), V1 != V2.
% etc...

% Also needed for first argument?
path_value(Instance,Path,Path) :- binary(Context,_,_,_,Path), instance(Instance,Context), constant(Path).
path_value(Instance,Path,N) :- binary(Context,_,_,_,Path), instance(Instance,Context), number(Path,N).

% Assume that a path only points to one instance at the moment
path(Instance,Path) :- binary(Context,_,Path,_,_), path(Path,0,_), instance(Instance,Context).
path(Instance,Path) :- binary(Context,_,_,_,Path), path(Path,0,_), instance(Instance,Context).

path_value(Instance,Path,V)    :- path(Instance,Path), path(Path,0,Name), not path(Path,1,_), value(Instance,Name,V).
path_value(Instance,Path,0,(Name,Instance)) :- path(Instance,Path), path(Path,0,Name), path(Path,1,_).

path_value(Instance,Path,V)    :- path_value(Instance,Path,N-1,Name0), path(Path,N,Name1), not path(Path,N+1,_), value(Name0,Name1,V).
path_value(Instance,Path,N,(Name1,Name0)) :- path_value(Instance,Path,N-1,Name0), path(Path,N,Name1), path(Path,N+1,_).


% #show instance/2.
% #show value/3.

#show path_value/3.

behavior((":root",0)).
condition((":root",0),"color=Yellow").
binary(":root","color=Yellow","color","=","Yellow").
path("color",0,"color").
constant("Yellow").
require((":root",0),"frontWheel.size>16").
binary(":root","frontWheel.size>16","frontWheel.size",">","16").
path("frontWheel.size",0,"frontWheel").
path("frontWheel.size",1,"size").
number("16",16).

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
binary(":root","frontWheel.size=rearWheel.size","frontWheel.size","=","rearWheel.size").
path("frontWheel.size",0,"frontWheel").
path("frontWheel.size",1,"size").
path("rearWheel.size",0,"rearWheel").
path("rearWheel.size",1,"size").



% Always include boolean enumeration
enumeration("bool").
option("bool", "True").
option("bool", "False").


