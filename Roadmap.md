# Roadmap for COOM with ASP project

## What has been achieved so far?
- Three COOM language fragments in increasing complexity
- Corresponding ASP fact format and ANTLR4 parser for COOM to ASP
    - Unit tests for parser
- Three corresponding encodings for the language fragments for clingo and fclingo
- Basic Python package to parse and solve COOM/ASP instances
- Two possible benchmark sets which are scalable: Restaurant and bike fleet
- Encodings from denkbares (correspond to current language fragments?)

## Supported COOM language fragments
- better names for the three instances/language fragments?

### Kids Bike
- No partonomy (no `structure` other than root of product)
- All features are enumerations with cardinality 1
- Enumerations can have attributes
    - Path expressions can therefore be of length one (`color`) or two (`frontWheel.size`)
- The following constraints are possible:
    - Single require
    - Single require with single condition
    - Combinations table


The following COOM language keywords are allowed:
- `structure(":root")`
- `feature`
- `enumeration`
- `attribute`
- `behavior`
- `condition` and `require`
    - followed by a simple boolean expression containing no logical operators, e.g., `color = Yellow`or `frontWheel.size > 16`
- `combinations`
- `allow`


### City Bike
In addition to the kids bike we have:
- Partonomy and cardinalities
    - Feature can now be Enumerations or Structures
    - Path expressions can thus be of arbitrary length
    - Only Structure features can have cardinalities

The following COOM language keywords are allowed additionally:
- `structure`
- Cardinalities, e.g., `0..1` in front of a (`structure`) feature
- `behavior PartName {}`, meaning the constraint is defined relative to part `PartName`

### Travel Bike
In addition to the city bike we have:
- Numerical features
- Aggregates `count`, `sum`, `min` and `max`
    - Arguments of aggregates are a single path expression
- Arithmetic calculations (`+`, `-`, `*`, `/`)
- Calculated values can be assigned to an attribute via the `imply` statement

The following COOM language keywords are allowed additionally:
- `num` (in front a a feature) together with a range, e.g., `1-100`
- `count(path.to.field)`
- `sum(path.to.field)`
- `min(path.to.field)`
- `max(path.to.field)`
- Arithmetic expressions, e.g., `path1 + path2 - count(path3)`
- `imply`

### What is NOT supported currently
- COOM allows nesting of conditions and requires. This is not supported by parser and encodings currently.
- COOM allows pointing to specific instances (e.g., first bag of carrier), although,
    this is not documented in the Quick Guide I found.
    Currently, the parser does not support this feature.
- Use of wildcards in tables is not supported
- forbid statement in tables is not supported
- Assumes that Enumeration and numeric features have cardinality 1
- Assumes that constant and numbers appear only on the right hand side of a binary relation
- Paths starting with `root.foo` are not supported
- Arithmetics with undefined terms will give UNSAT

#### fclingo
- Currently no division. Is this supported in fclingo?
- fclingo only supports linear constraints, so multiplication is only allowed
  if one of the terms is a  constant number
- Only if attributes are marked as numeric, fclingo will use treat them as such.
  Outside of tables it is not possible to compare non-numeric with numeric attributes.


## Open Questions

### Encoding
- How to handle SI units?
    - Should there be a conversion by the parser to some base unit? Simple to implement but maybe an advanced feature which we do not want in the paper
    - Or should all numerics be specified without SI units, thus in the same unit?
    - Or allow different units and user has to build in conversion into constraint, e.g., as is done for travel bike currently?
- How should arithmetics with undefined terms be handled?

### Python package
- Should the `solve` option take a COOM file or ASP instance as input?
    - The former would imply automatic conversion of the COOM file
    - The latter would give more flexibility to pass more than one ASP instance to the solver
- How to name the Python package?
    - coomsuite
    - coompiler
    - coompressor
    - coom2asp
    - coomutils
    - coomgo
    - coolingo

## Future Goals
- Write unit tests for the ASP encodings
- Create scalable benchmark sets for the three language features
- Publish paper introducing the three COOM language fragments, the encodings and the benchmark results (publish benchmarks on GitHub)
- Implement more COOM language features in the parser and the encodings
- Add visualization option to Python package (clingraph or clinguin)
- Add interactivity to Python package using clinguin
- Write more encodings, e.g., order encoding for numeric values



