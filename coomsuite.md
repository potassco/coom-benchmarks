# COOM Suite

## Basic functionality from 2024 LPNMR paper
- Three COOM language fragments in increasing complexity
- Corresponding ASP fact format and ANTLR4 parser for COOM to ASP
    - Unit tests for parser
- Encodings for clingo and flingo
- Basic Python package to parse and solve COOM/ASP instances
- Four scalable benchmark sets: Random Core, Restaurant, City Bike Fleet, Travel Bike Fleet

## Extensions for TPLP paper
- UI
- User Input (`set` values and `add` objects)
- Simple approach for solving (unbounded) instances incrementally, single-shot only (i.e., for each bound preprocess the serialized "COOM" facts from scratch)

## In the meantime...
- Added documentation
- Added thorough testing for the encodings
- Made release v1.0.0
- Extended incremental approach with clingo Multi-shot encoding (possible paper for ASPOCP'26)
- Support for optimization (`minimize`/`maximize` keyword in COOM)
- Other minor updates to implementation

## Work in progress or almost finished
- Added support for associations (`reference` keyword in COOM)
    - important for the "Racks" and "House" problem (from Siemens) and "Warema blinds" problem
    - implemented user input for associations
    - some open questions on how to best represent this in ASP (possible think tank later this month)
- Started implementing "Navigation/Exploring solution space" features
    - this functionality will go into a separate `clinteract` repo, Susana is involved here
- Constraint Handler encoding
    - functional but waiting for a stable constraint handler version to integrate into main repo
- Created new benchmark sets and refined existing ones
    - 1 Benchmark set in COOM Core language: "Random Core"
    - 3 Benchmark sets with linear numerical constraints: "Bike Fleet", "Metro", "Restaurant"
    - 1 Benchmark set with quadratic, numerical constraints: "Box"
    - "Space Collider" is real-world, anonymized benchmark from denkbares. 3 very large instances.
    - 3 Benchmark sets for unbounded cardinalities: "Cargo Bike" (from denkbares) and "Racks" and "House" Problem (from Siemens)
    - Next steps:
        - Create benchmarks from "Shadow Master" (for ConfWS'26) that subsumes all topics from PANKO: unbounded cardinalities, non-trivial numerical calculations (trigonometric, square root,...)
        - denkbares has a student working on the "Espresso machine", possible benchmark but probably ready only later this year
        - Run and evaluate benchmarks on cluster
        - Add and evaluate alternative encodings (existing encodings are not written for performance but for clear representation)

## Misc
- Experimented with representing and solving study regulation problems
    - fruitful, led to (experimental) implementation of some new language features but also showed limitations of current way COOM
        and our fact format is constructed


## Future work
- Support for more complex defaults
    - currently only simple defaults are implemented which can be overriden by user input but do not handle indirect forms of inconsistencies
- Improve encodings (see "Benchmarks")
- Improvements to COOM language?
    - not a priority for us at the moment I would say but if we decided to use COOM on a larger scale
- Re-evaluation of fact format
    - implemented many new features since original version
    - is the fact format scalable? see "Space Collider" benchmark
- Add clingraph encoding
- UI: Waiting for clinguin API to integrate into Python
- Can we generalize user input, e.g. express simple constraints instead of just setting single values
- What calculations are post-processing?
