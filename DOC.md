# Instance
The instances are generated automatically by parsing a COOM file. We describe here the ASP fact format used for the translation.

### Structure
A COOM product can be made up of a hierarchical component structure.
The building blocks of the product can be defined by the predicate `structure/1`.

> **Note:** Every product has at least the `structure(":root")` predicate at the top of the hierarchy.

```prolog
structure(Name).
```

Parameters:
- `Name` - Name of the structure

Examples:
```prolog
structure(":root").
structure("Carrier").
```

### Name
Description

```prolog
Abstract Specification
```

Parameters:
- `Parameter1` - Description1

Examples:
```prolog
name(...)
```

### Name
Description

```prolog
Abstract Specification
```

Parameters:
- `Parameter1` - Description1

Examples:
```prolog
name(...)
```

# Encoding
