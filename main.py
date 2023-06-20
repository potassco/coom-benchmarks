from sys import argv
from typing import Optional

from antlr4 import FileStream, CommonTokenStream
from model.ModelLexer import ModelLexer
from model.ModelParser import ModelParser
from model.ModelVisitor import ModelVisitor


class ASPVisitor(ModelVisitor):

    def __init__(self):
        super().__init__()
        self.parent_enum: Optional[ModelParser.EnumerationContext] = None


# def visitProduct(self, ctx:ModelParser.ProductContext):
#     print(f"structure(\":root\").")
#     super().visitProduct(ctx)

# def visitStructure(self, ctx:ModelParser.StructureContext):
#     print(f"structure({ctx.name().getText()}).")
#     super().visitStructure(ctx)

# def visitFeature(self, ctx:ModelParser.FeatureContext):
#     field: ModelParser.FieldContext = ctx.field()
#     if field.number_def() is not None:
#         type_name = "num"
#     elif field.string_def() is not None:
#         type_name = "text"
#     else:
#         # this seems hacky, I couldn't figure out how to do it better on the hurry
#         try:
#             type_name = '"' + field.type_ref().name().getText() + '"'
#         except TypeError:
#             type_name = '":root"'
#     feature_name = '"' + field.fieldName.getText() + '"'
#     cardinality: ModelParser.CardinalityContext = ctx.cardinality()
#     c_min = 1 if cardinality is None else cardinality.min
#     c_max = 1 if cardinality is None else cardinality.max
#     print(f"feature({type_name}, {feature_name}, {c_min}, {c_max}).")

# def visitEnumeration(self, ctx:ModelParser.EnumerationContext):
#     self.parent_enum = ctx
#     print(f"enumeration(\"{ctx.name().getText()}\").")
#     super().visitEnumeration(ctx)
#     self.parent_enum = None

# def visitOption(self, ctx:ModelParser.OptionContext):
#     if self.parent_enum is None:
#         raise ValueError("illegal option")
#     parent_name = '"' + self.parent_enum.name().getText() + '"'
#     option_name = '"' + ctx.name().getText() + '"'
#     print(f"option({parent_name}, {option_name}).")

# def visitBehavior(self, ctx: ModelParser.BehaviorContext):
#     print(ctx.getRuleIndex())
#     return super().visitBehavior(ctx)

if __name__ == "__main__":
    input_stream = FileStream(argv[1])
    lexer = ModelLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ModelParser(stream)
    tree = parser.root()
    visitor = ASPVisitor()
    visitor.visitRoot(tree)
