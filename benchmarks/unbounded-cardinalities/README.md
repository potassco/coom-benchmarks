# Unbounded Cardinalities Benchmarks

The COOM Suite contains the following sets of benchmarks for the **COOM[X\*]**
language.

In all benchmark sets the minimal satisfiable bound for the unbounded
cardinalities is scaled through the addition of user input.

Furthermore, some of the benchmark sets can also be scaled via certain domain
sizes, resulting in larger configuration spaces.

## Cargo Bike

- Two variations of the cargo bike with increasing complexity
- The domain size of volume attributes can be scaled
- User inputs on the requested volume scale the minimal satisfiable bound

## Racks

- Two variations of the racks problem [[1]](#1) with increasing complexity
- User inputs on the required number of elements scale the minimal satisfiable
  bound

## House

- A benchmark set based on the house configuration problem [[2]](#2)
- The domain sizes of the number of rooms, and number of things can be scaled
- Additionally the number of persons scales the instance
- User inputs on the number of things per person scale the minimal satisfiable
  bound


## References

<a id="1">[1]</a>
A. A. Falkner, A. Ryabokon, G. Schenner, K. M. Shchekotykhin (2015).
**OOASP: Connecting Object-Oriented and Logic Programming**.
Proceedings of the Thirteenth International Conference on Logic Programming
and Nonmonotonic Reasoning (LPNMR’15), 9345, 332-345, Springer (2015).
https://doi.org/10.1007/978-3-319-23264-5_28.

<a id="2">[2]</a>
G. Friedrich, A. Ryabokon, A. A. Falkner, A. Haselböck, G. Schenner, H. Schreiner. (2011).
**(Re)configuration using Answer Set Programming**.
Proceedings of the Second Workshop on Logics for Component Configuration (LoCoCo'11), 65, 26-35, EPCTS (2011).
https://doi.org/10.4204/EPTCS.65.3.




