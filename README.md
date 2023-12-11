# COOM Parser and Encoding

A parser to translate COOM DSL into ASP facts
plus a corresponding encoding.

## Installation
For the parser install ANTLR4 for python
```
pip install antlr4-tools
pip install antlr4-python-runtime
```

The `model` directory contains is provided by denkbares and represents the current state of the COOM DSL language.


More information on the ANTLR4 python target can be found here:
https://github.com/antlr/antlr4/blob/master/doc/python-target.md


## Usage
### Parser

To parse a `.coom` file run
```
python parse.py FILE.coom > OUTPUT.lp
```
Replace `FILE` and `OUTPUT` with the desired filenames.
The `parse.py` script itself just prints the ASP facts to the console.

### Testing
To test the parser run (the Python `unittest` package needs to be installed)
```
python -m unittest tests/tests_parser.py
```
