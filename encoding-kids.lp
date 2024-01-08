instance((),":root") :- structure(":root").

% Always generate minimal number of objects
instance((Feature,(Instance,0..Min-1)),Type)      :- feature(Context,Feature,Type,Min,_),      enumeration(Type),    instance(Instance,Context).

% Optionally generate additional objects
{ instance((Feature,(Instance,Idx)),Type)      : Idx = Min..Max-1 } :- feature(Context,Feature,Type,Min,Max),      enumeration(Type),    instance(Instance,Context).

% Indices in ascending order
:- instance((Feature,(Instance,Idx)),_), not instance((Feature,(Instance,Idx-1)),_), Idx > 0.
% Generate enumeration and attribute values
{ value(Instance,Option) : option(Type,Option) } :- instance(Instance,Type).
:-  { value(Instance,Option) : option(Type,Option) } != 1, enumeration(Type), instance(Instance,Type).

% Derive associated attribute values
% TODO: Is an index (0) needed in the path for the sake of uniformity?
value((Attr,(Instance,0)),V) :- attr_value(Type,Option,Attr,V), instance(Instance,Type), value(Instance,Option).



%%% Constraints
constraint(Instance,(Context,Idx)) :- behavior((Context,Idx)), instance(Instance,Context).
:- constraint(Instance,Constraint), unsat(Instance,Constraint).

% TODO: Need to check for multiple conditions or requires (or nested), convert to propositional formula? or use unsat atoms?
unsat(Instance,Constraint) :- condition_sat(Instance,Constraint), not require_sat(Instance,Constraint).
% TODO: Is this correct?
unsat(Instance,Constraint) :- constraint(Instance,Constraint), require(Constraint,_), not condition(Constraint,_), not require_sat(Instance,Constraint).
% Combinations Table (only for allow)
unsat(Instance,Constraint) :- constraint(Instance,Constraint), combinations(Constraint,_,_), not hit_row(Instance,Constraint,_).

% Satisfaction atoms for different constraint types
condition_sat(Instance,Constraint) :- constraint(Instance,Constraint), condition(Constraint,Formula), binary_sat(Instance,Formula).
require_sat(Instance,Constraint)   :- constraint(Instance,Constraint), require(Constraint,Formula), binary_sat(Instance,Formula).

% Satisfaction atoms for binary relations
% TODO: Assumes that a path points to one value only
binary_values(Instance,Formula,V1,Operator,V2) :- binary(Context,Formula,Path1,Operator,Path2), instance(Instance,Context),
                                                value(Instance,Path1,V1),
                                                value(Instance,Path2,V2).
binary_sat(Instance,Formula) :- binary_values(Instance,Formula,V1,"=",V2), V1 = V2.
binary_sat(Instance,Formula) :- binary_values(Instance,Formula,V1,"!=",V2), V1 != V2.
binary_sat(Instance,Formula) :- binary_values(Instance,Formula,V1,">",V2), V1 > V2.
binary_sat(Instance,Formula) :- binary_values(Instance,Formula,V1,">=",V2), V1 >= V2.
binary_sat(Instance,Formula) :- binary_values(Instance,Formula,V1,"<",V2), V1 < V2.
binary_sat(Instance,Formula) :- binary_values(Instance,Formula,V1,"<=",V2), V1 <= V2.

%%% Get values of path expressions
path_instance(Instance,Path) :- binary(Context,_,Path,_,_),       path(Path,0,_), instance(Instance,Context).
path_instance(Instance,Path) :- binary(Context,_,_,_,Path),       path(Path,0,_), instance(Instance,Context).
path_instance(Instance,Path) :- combinations((Context,_),_,Path), path(Path,0,_), instance(Instance,Context).
path_instance(Instance,Path) :- function(Context,_,_,Path),       path(Path,0,_), instance(Instance,Context).

path_value(Instance,Path,Instance2,V)      :- path_instance(Instance,Path), path(Path,0,Name), not path(Path,1,_), value(Instance2,V),    Instance2=(Name,(Instance,_)).
path_value(Instance,Path,Instance2,object) :- path_instance(Instance,Path), path(Path,0,Name), not path(Path,1,_), instance(Instance2,_), Instance2=(Name,(Instance,_)).
path_instance(Instance,Path,0,Instance2)   :- path_instance(Instance,Path), path(Path,0,Name),     path(Path,1,_), instance(Instance2,_), Instance2=(Name,(Instance,_)).

path_value(Instance,Path,Instance3,V)      :- path_instance(Instance,Path,N-1,Instance2), path(Path,N,Name), not path(Path,N+1,_), value(Instance3,V)   , Instance3=(Name,(Instance2,_)).
path_value(Instance,Path,Instance3,object) :- path_instance(Instance,Path,N-1,Instance2), path(Path,N,Name), not path(Path,N+1,_), instance(Instance3,_), Instance3=(Name,(Instance2,_)).
path_instance(Instance,Path,N,Instance3)   :- path_instance(Instance,Path,N-1,Instance2), path(Path,N,Name),     path(Path,N+1,_), instance(Instance3,_), Instance3=(Name,(Instance2,_)).

% Constants and numbers
% TODO: Also needed for first argument?
path_value(Instance,Path,constant,Path) :- binary(Context,_,_,_,Path), instance(Instance,Context), constant(Path).
path_value(Instance,Path,number,N)      :- binary(Context,_,_,_,Path), instance(Instance,Context), number(Path,N).

value(Instance,Path,V) :- path_value(Instance,Path,_,V), V != object.

%%% Check combinations
% TODO: Currently assumes that there is only one possible attribute at end of path
% TODO: Only checks allow. Add forbid statements
% TODO: Does this check for wildcards?
hit_cell(Instance,Constraint,(Col,Row)) :- allow(Constraint,(Col,Row),V), combinations(Constraint,Col,Path),
                                            constraint(Instance,Constraint), value(Instance,Path,V).
hit_row(Instance,Constraint,Row) :- allow(Constraint,(_,Row),_), constraint(Instance,Constraint),
                                    0 = #sum{ 1,Col: allow(Constraint,(Col,Row),_); -1,Col': hit_cell(Instance,Constraint,(Col',Row)) }.


% Always include boolean enumeration
enumeration("bool").
option("bool", "True").
option("bool", "False").

#show instance/2.
#show value/2.

#defined structure/1.
#defined feature/5.
#defined enumeration/1.
#defined option/2.
#defined attribute/2.
#defined attr_value/4.
#defined behavior/1.
#defined require/2.
#defined condition/2.
#defined imply/3.
#defined combinations/3.
#defined allow/3.
#defined binary/5.
#defined function/4.
#defined path/3.
#defined constant/1.
#defined number/2.
