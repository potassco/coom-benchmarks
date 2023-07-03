"""
Basic functions to run tests.
"""
from io import StringIO
from unittest.mock import patch

from antlr4 import InputStream, CommonTokenStream
from model.ModelLexer import ModelLexer
from model.ModelParser import ModelParser

from parse import ASPVisitor


def parse_coom(coom_input):
    input_stream = InputStream(coom_input)
    lexer = ModelLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ModelParser(stream)
    tree = parser.root()
    visitor = ASPVisitor()
    with patch('sys.stdout', new=StringIO()) as fake_out:
        visitor.visitRoot(tree)
        output_list = fake_out.getvalue().split('\n')
        output_list = output_list[:-1] if output_list[-1] == '' else output_list
        return output_list


def make_list(facts):
    return facts.split('\n')
