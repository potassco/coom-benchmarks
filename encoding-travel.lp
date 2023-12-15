instance((),":root") :- structure(":root").

% Always generate minimal number of objects
instance((Feature,(Instance,0..Min-1)),Structure) :- feature(Context,Feature,Structure,Min,_), structure(Structure), instance(Instance,Context).
instance((Feature,(Instance,0..Min-1)),Type)      :- feature(Context,Feature,Type,Min,_),      enumeration(Type),    instance(Instance,Context).

% Optionally generate additional objects
{ instance((Feature,(Instance,Idx)),Structure) : Idx = Min..Max-1 } :- feature(Context,Feature,Structure,Min,Max), structure(Structure), instance(Instance,Context).
{ instance((Feature,(Instance,Idx)),Type)      : Idx = Min..Max-1 } :- feature(Context,Feature,Type,Min,Max),      enumeration(Type),    instance(Instance,Context).

% Indices in ascending order
:- instance((Feature,(Instance,Idx)),_), not instance((Feature,(Instance,Idx-1)),_), Idx > 0.

% Generate enumeration and attribute values
{  value(Instance,Option) : option(Type,Option) } :- instance(Instance,Type).
:-  {  value(Instance,Option) : option(Type,Option) } != 1, enumeration(Type), instance(Instance,Type).

% Derive associated attribute values
% TODO: Is an index needed in the path for the sake of uniformity?
value((Attr,Instance),V):- attr_value(Type,Option,Attr,V), instance(Instance,Type), value(Instance,Option).



%%% Constraints
constraint(Instance,(Context,Idx)) :- behavior((Context,Idx)), instance(Instance,Context).
% :- constraint(Instance,Constraint), unsat(Instance,Constraint).

% TODO: Need to check for multiple conditions or requires (or nested), converto propositional formula? or use unsat atoms?
unsat(Instance,Constraint) :- condition_sat(Instance,Constraint), not require_sat(Instance,Constraint).
% TODO: Is this correct?
unsat(Instance,Constraint) :- constraint(Instance,Constraint), require(Constraint,_), not condition(Constraint,_), not require_sat(Instance,Constraint).
% Combinations Table (only for allow)
unsat(Instance,Constraint) :- constraint(Instance,Constraint), combinations(Constraint,_,_), not hit_row(Instance,Constraint,_).

% Satisfaction atoms for different constraint types
condition_sat(Instance,Constraint) :- constraint(Instance,Constraint), condition(Constraint,Formula), binary_sat(Instance,Formula).
require_sat(Instance,Constraint)   :- constraint(Instance,Constraint), require(Constraint,Formula), binary_sat(Instance,Formula).

% Satisfaction atoms for binary relations
binary_values(Instance,Formula,V1,Operator,V2) :- binary(Context,Formula,Path1,Operator,Path2), instance(Instance,Context),
                                                path_value(Instance,Path1,V1),
                                                path_value(Instance,Path2,V2).
binary_sat(Instance,Formula) :- binary_values(Instance,Formula,V1,"=",V2), V1 = V2.
binary_sat(Instance,Formula) :- binary_values(Instance,Formula,V1,"!=",V2), V1 != V2.
binary_sat(Instance,Formula) :- binary_values(Instance,Formula,V1,">",V2), V1 > V2.
binary_sat(Instance,Formula) :- binary_values(Instance,Formula,V1,">=",V2), V1 >= V2.
binary_sat(Instance,Formula) :- binary_values(Instance,Formula,V1,"<",V2), V1 < V2.
binary_sat(Instance,Formula) :- binary_values(Instance,Formula,V1,"<=",V2), V1 <= V2.

%%% Get values of path expressions
% Also needed for first argument?
path_value(Instance,Path,Path) :- binary(Context,_,_,_,Path), instance(Instance,Context), constant(Path).
path_value(Instance,Path,N) :- binary(Context,_,_,_,Path), instance(Instance,Context), number(Path,N).

% Assume that a path only points to one instance at the moment
path(Instance,Path) :- binary(Context,_,Path,_,_), path(Path,0,_), instance(Instance,Context).
path(Instance,Path) :- binary(Context,_,_,_,Path), path(Path,0,_), instance(Instance,Context).
path(Instance,Path) :- combinations((Context,_),_,Path), path(Path,0,_), instance(Instance,Context).

path_value(Instance,Path,V)    :- path(Instance,Path), path(Path,0,Name), not path(Path,1,_), value(Instance,Name,V).
path_value(Instance,Path,0,(Name,Instance)) :- path(Instance,Path), path(Path,0,Name), path(Path,1,_).

path_value(Instance,Path,V)    :- path_value(Instance,Path,N-1,Name0), path(Path,N,Name1), not path(Path,N+1,_), value(Name0,Name1,V).
path_value(Instance,Path,N,(Name1,Name0)) :- path_value(Instance,Path,N-1,Name0), path(Path,N,Name1), path(Path,N+1,_).

%%% Check combinations
% TODO: Currently assumes that there is only one possible attribute at end of path
% TODO: Only checks forbid
hit_cell(Instance,Constraint,(Col,Row)) :- allow(Constraint,(Col,Row),V), combinations(Constraint,Col,Path), 
                                            constraint(Instance,Constraint), path_value(Instance,Path,V).
hit_row(Instance,Constraint,Row) :- allow(Constraint,(_,Row),_), constraint(Instance,Constraint),
                                    0 = #sum{ 1,Col: allow(Constraint,(Col,Row),_); -1,Col': hit_cell(Instance,Constraint,(Col',Row)) }.



#show instance/2.
#show value/2.




% Always include boolean enumeration
enumeration("bool").
option("bool", "True").
option("bool", "False").


