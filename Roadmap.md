# Roadmap for COOM with ASP project


## Supported COOM language fragments

- better names?

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
- Cardinalities, e.g., `0..1` in front of a (`Structure`) feature
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

## Future Goals
