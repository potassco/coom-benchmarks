instance((),":root") :- structure(":root").

% Always generate minimal number of objects
instance((Feature,(Instance,0..Min-1)),Structure) :- feature(Context,Feature,Structure,Min,_), structure(Structure), instance(Instance,Context).

% Optionally generate additional objects
{ instance((Feature,(Instance,Idx)),Structure) : Idx = Min..Max-1 } :- feature(Context,Feature,Structure,Min,Max), structure(Structure), instance(Instance,Context).

% Indices in ascending order
:- instance((Feature,(Instance,Idx)),_), not instance((Feature,(Instance,Idx-1)),_), Idx > 0.

% Generate enumeration and attribute values
instance((Feature,(Instance,0)),Type) :- feature(Context,Feature,Type,Min,_), enumeration(Type), instance(Instance,Context).
{ val((Instance),Option) : option(Type,Option) } :- instance(Instance,Type).
:-  { val(Instance,Option) : option(Type,Option) } != 1, enumeration(Type), instance(Instance,Type).

% Derive associated attribute values (the index 0 is needed for the sake of uniformity)
val((Attr,(Instance,0)),V)       :- attribute(Type,Attr,"str"), attr_value(Type,Option,Attr,V),
                                    instance(Instance,Type), val(Instance,Option).
&in{V..V} =: (Attr,(Instance,0)) :- attribute(Type,Attr,"num"), attr_value(Type,Option,Attr,V),
                                    instance(Instance,Type), val(Instance,Option).

% Assign numeric feature to a value
&in{Min..Max} =: (Feature,(Instance,0)) :- feature(Context,Feature,"num",_,_), range(Context,Feature,Min,Max), instance(Instance,Context).

% Create auxiliary instance predicate for paths
instance((Attr,(Instance,0)),Attr) :- attr_value(Type,_,Attr,_), instance(Instance,Type).
instance((Feature,(Instance,0)),Feature) :- feature(Context,Feature,"num",_,_), instance(Instance,Context).

%%% Constraints
% Instantiate constraint for each instance
constraint(Instance,(Context,Idx)) :- behavior((Context,Idx)), instance(Instance,Context).
:- constraint(Instance,Constraint), unsat(Instance,Constraint).

% Require without condition
unsat(Instance,Constraint) :- condition(Constraint,CBinary),     require(Constraint,RBinary),
                              binary_sat(Instance,CBinary),  not binary_sat(Instance,RBinary),
                              constraint(Instance,Constraint).
% Require with condition
unsat(Instance,Constraint) :- not condition(Constraint,_),     require(Constraint,Binary),
                              constraint(Instance,Constraint), not binary_sat(Instance,Binary).
% Combinations Table (only for allow)
unsat(Instance,Constraint) :- combinations(Constraint,_,_),
                              constraint(Instance,Constraint), not hit_row(Instance,Constraint).


% Satisfaction of binary relations
binary_instance(Instance,Formula,Path1,Operator,Path2) :- binary(Context,Formula,Path1,Operator,Path2), instance(Instance,Context).
binary_values(Instance,Formula,V1,Operator,V2) :- binary_instance(Instance,Formula,Path1,Operator,Path2),
                                                path_value(Instance,Path1,V1),
                                                path_value(Instance,Path2,V2).

binary_sat(Instance,Formula) :- binary_values(Instance,Formula,V1,"=",V2),  V1 = V2.
binary_sat(Instance,Formula) :- binary_values(Instance,Formula,V1,"!=",V2), V1 != V2.
binary_sat(Instance,Formula) :- binary_values(Instance,Formula,V1,">",V2),  V1 > V2.
binary_sat(Instance,Formula) :- binary_values(Instance,Formula,V1,">=",V2), V1 >= V2.
binary_sat(Instance,Formula) :- binary_values(Instance,Formula,V1,"<",V2),  V1 < V2.
binary_sat(Instance,Formula) :- binary_values(Instance,Formula,V1,"<=",V2), V1 <= V2.

binary_sat(Instance,Formula) :- binary_instance(Instance,Formula,Path1,"=",Path2), &sum{path_value(Instance,Path1)} =  path_value(Instance,Path2).
binary_sat(Instance,Formula) :- binary_instance(Instance,Formula,Path1,"!=",Path2) &sum{path_value(Instance,Path1)} != path_value(Instance,Path2).
binary_sat(Instance,Formula) :- binary_instance(Instance,Formula,Path1,">",Path2), &sum{path_value(Instance,Path1)} >  path_value(Instance,Path2).
binary_sat(Instance,Formula) :- binary_instance(Instance,Formula,Path1,">=",Path2) &sum{path_value(Instance,Path1)} >= path_value(Instance,Path2).
binary_sat(Instance,Formula) :- binary_instance(Instance,Formula,Path1,"<",Path2), &sum{path_value(Instance,Path1)} <  path_value(Instance,Path2).
binary_sat(Instance,Formula) :- binary_instance(Instance,Formula,Path1,"<=",Path2) &sum{path_value(Instance,Path1)} <= path_value(Instance,Path2).

%%% Get values of path expressions
path_instance(Instance,Path) :- binary(Context,_,Path,_,_),       path(Path,0,_), instance(Instance,Context).
path_instance(Instance,Path) :- binary(Context,_,_,_,Path),       path(Path,0,_), instance(Instance,Context).
path_instance(Instance,Path) :- combinations((Context,_),_,Path), path(Path,0,_), instance(Instance,Context).
path_instance(Instance,Path) :- function(Context,_,_,Path), path(Path,0,_), instance(Instance,Context).

path_instance(Instance,Path,0,Instance2) :- path(Path,0,Name),
                                            path_instance(Instance,Path), instance(Instance2,_), Instance2=(Name,(Instance,_)).
path_instance(Instance,Path,N,Instance3) :- path(Path,N,Name),
                                            path_instance(Instance,Path,N-1,Instance2), instance(Instance3,_), Instance3=(Name,(Instance2,_)).

path_value(Instance,Path,Instance2,V) :- not path(Path,N+1,_), path_instance(Instance,Path,N,Instance2), val(Instance2,V).
path_value(Instance,Path,V) :- path_value(Instance,Path,Instance2,V).

&sus{ Instance2 } =: path_value(Instance,Path,Instance2) :- not path(Path,N+1,_), path_instance(Instance,Path,N,Instance2).
&sus{ Instance2 } =: path_value(Instance,Path) :- not path(Path,N+1,_), path_instance(Instance,Path,N,Instance2).

% Paths which point to instances (not attributes)
path_object(Instance,Path,Instance2) :- not path(Path,N+1,_), path_instance(Instance,Path,N,Instance2), not val(Instance2,_).

% Constants and numbers
% TODO: Also needed for first argument?
path_value(Instance,Path,constant,Path) :- binary(Context,_,_,_,Path), instance(Instance,Context), constant(Path).
&in{N..N} =: path_value(Instance,Path) :- binary(Context,_,_,_,Path), instance(Instance,Context), number(Path,N).

%%% Check combinations
hit_cell(Instance,Constraint,(Col,Row)) :- allow(Constraint,(Col,Row),V), combinations(Constraint,Col,Path),
                                            constraint(Instance,Constraint), path_value(Instance,Path,V).
hit_cell(Instance,Constraint,(Col,Row)) :- allow(Constraint,(Col,Row),V), combinations(Constraint,Col,Path),
                                            constraint(Instance,Constraint), &sum{path_value(Instance,Path)} = V.
hit_row(Instance,Constraint) :- allow(Constraint,(_,Row),_), constraint(Instance,Constraint),
                                    0 = #sum{ 1,Col: allow(Constraint,(Col,Row),_); -1,Col': hit_cell(Instance,Constraint,(Col',Row)) }.

% % Evaluate functions (aggregates)
% % Assumes that every function and every term in an arithmetic expression points to a single path
% % path_value(Instance,Function,V) :- function(Context,Function,"count",Path), instance(Instance,Context), V = #count{ V',Instance2: path_value(Instance,Path,Instance2,V') }.

% &sus{ 1,Instance2: path_object(Instance,Path,Instance2) } =: path_value(Instance,Function)
%                         :- function(Context,Function,"count",Path), instance(Instance,Context).

% &sus{ Instance2 : path_instance(Instance,Path,Instance2) } =: path_value(Instance,Function)
%                         :- function(Context,Function,"sum",Path), instance(Instance,Context).

% path_value(Instance,Function,V) :- function(Context,Function,"min",Path),   instance(Instance,Context), V = #min  { V',Instance2: path_value(Instance,Path,Instance2,V') }.
% path_value(Instance,Function,V) :- function(Context,Function,"max",Path),   instance(Instance,Context), V = #max  { V',Instance2: path_value(Instance,Path,Instance2,V') }.

% % Arithmetics
% % path_value(Instance,Formula,V1+V2) :- binary(Context,Formula,Left,"+",Right), instance(Instance,Context), path_value(Instance,Left,V1), path_value(Instance,Right,V2).
% &sus{ path_value(Instance,Left); path_value(Instance,Right) } =: path_value(Instance,Formula) :- binary(Context,Formula,Left,"+",Right),
%                                                 instance(Instance,Context), path_instance(Instance,Left,LI), path_instance(Instance,Right,RI).

% path_value(Instance,Formula,V1-V2) :- binary(Context,Formula,Left,"-",Right), instance(Instance,Context), path_value(Instance,Left,V1), path_value(Instance,Right,V2).
% path_value(Instance,Formula,V1*V2) :- binary(Context,Formula,Left,"*",Right), instance(Instance,Context), path_value(Instance,Left,V1), path_value(Instance,Right,V2).
% % TODO: Add more arithmetics

% % Imply statements
% &sus{ path_value(Instance,Formula) } =: (Name,(Instance,0)) :- imply((Context,_),Name,Formula), instance(Instance,Context).


% Always include boolean enumeration
enumeration("bool").
option("bool", "True").
option("bool", "False").

% #show instance(I,S) : instance(I,S), structure(S).
% #show instance/2.
#show val/2.
#show.
% &show { (Feature,(Instance,0)) : feature(Context,Feature,"num",_,_), instance(Instance,Context) }.
% &show { (Attr,(Instance,0))    : attribute(Type,Attr,"num"),         instance(Instance,Type) }.


#defined structure/1.
#defined feature/5.
#defined range/4.
#defined enumeration/1.
#defined option/2.
#defined attribute/3.
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
#defined imply/3.
#defined function/4.

