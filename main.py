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
        # self.parent_behavior: Optional[ModelParser.BehaviorContext] = None
        self.behavior_name: str = '":root"'
        self.constraint_idx: int = 0
        self.path_idx: int = 0

    def visitProduct(self, ctx: ModelParser.ProductContext):
        print("structure(\":root\").")
        super().visitProduct(ctx)

    def visitStructure(self, ctx: ModelParser.StructureContext):
        print(f"structure({ctx.name().getText()}).")
        super().visitStructure(ctx)

    def visitEnumeration(self, ctx: ModelParser.EnumerationContext):
        self.parent_enum = ctx
        print(f"enumeration(\"{ctx.name().getText()}\").")
        super().visitEnumeration(ctx)
        self.parent_enum = None

    def visitBehavior(self, ctx: ModelParser.BehaviorContext):
        if ctx.name() is not None:
            self.parent_behavior = ctx.name().getText()
        # behavior_block: ModelParser.Behavior_blockContext = ctx.behavior_block(
        # )
        # try:
        #     print(behavior_block.conditioned(0).precondition(0).getText())
        # except AttributeError:
        #     pass
        # require: ModelParser.RequireContext = behavior_block.conditioned(
        #     0).require()
        # if require is not None:
        #     print(require.getText())
        #     print(require.condition().condition_or().condition_and(
        #         0).condition_not(0).condition_compare().condition_part(
        #             0).getText())
        super().visitBehavior(ctx)
        self.parent_behavior = '":root"'

    def visitFeature(self, ctx: ModelParser.FeatureContext):
        field: ModelParser.FieldContext = ctx.field()
        if field.number_def() is not None:
            type_name = "num"
        elif field.string_def() is not None:
            type_name = "text"
        else:
            # this seems hacky, I couldn't figure out how to do it better on the hurry
            try:
                type_name = '"' + field.type_ref().name().getText() + '"'
            except TypeError:
                type_name = '":root"'
        feature_name = '"' + field.fieldName.getText() + '"'
        cardinality: ModelParser.CardinalityContext = ctx.cardinality()
        c_min = 1 if cardinality is None else cardinality.min
        c_max = 1 if cardinality is None else cardinality.max
        print(f"feature({type_name}, {feature_name}, {c_min}, {c_max}).")

    def visitAttribute(self, ctx: ModelParser.AttributeContext):
        if self.parent_enum is None:
            raise ValueError("illegal option")
        parent_name = '"' + self.parent_enum.name().getText() + '"'
        field: ModelParser.FieldContext = ctx.field()
        field_name = '"' + field.fieldName.getText() + '"'
        print(f'attribute({parent_name},{field_name}).')
        super().visitAttribute(ctx)

    def visitOption(self, ctx: ModelParser.OptionContext):
        if self.parent_enum is None:
            raise ValueError("illegal option")
        parent_name = '"' + self.parent_enum.name().getText() + '"'
        option_name = '"' + ctx.name().getText() + '"'
        print(f"option({parent_name}, {option_name}).")

        constant: ModelParser.ConstantContext = ctx.constant()
        if constant != []:
            parent_attr: ModelParser.AttributeContext = self.parent_enum.attribute(
            )
            for a, c in zip(parent_attr, constant):
                field: ModelParser.FieldContext = a.field()
                attr_name = '"' + field.fieldName.getText() + '"'
                option_value = c.floating().getText()
                print(
                    f'value({parent_name},{option_name},{attr_name},{option_value}).'
                )

    def visitConditioned(self, ctx: ModelParser.ConditionedContext):
        # name = self.behavior_name if self.behavior_name is not None else '":root"'
        print(f'behavior({self.behavior_name},{self.constraint_idx}).')
        super().visitConditioned(ctx)
        self.constraint_idx += 1

    def visitCombinations(self, ctx: ModelParser.CombinationsContext):
        for f in ctx.formula():
            print(
                f'combinations({self.behavior_name},{self.constraint_idx},path{self.path_idx}).'
            )
            print(f.formula_add().formula_sub(0).formula_mul(0).getText())
            self.path_idx += 1
        super().visitCombinations(ctx)


if __name__ == "__main__":
    input_stream = FileStream(argv[1])
    lexer = ModelLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ModelParser(stream)
    tree = parser.root()
    visitor = ASPVisitor()
    visitor.visitRoot(tree)
