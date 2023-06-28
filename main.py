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
        self.behavior_name: str = ':root'
        self.constraint_idx: int = 0
        # self.path_idx: int = 0
        self.row_idx: int = 0
        self.cond_idx: int = 0
        self.print_path: bool = True

    def visitProduct(self, ctx: ModelParser.ProductContext):
        print('structure(":root").')
        super().visitProduct(ctx)

    def visitStructure(self, ctx: ModelParser.StructureContext):
        print(f'structure("{ctx.name().getText()}").')
        super().visitStructure(ctx)

    def visitEnumeration(self, ctx: ModelParser.EnumerationContext):
        self.parent_enum = ctx
        print(f'enumeration("{ctx.name().getText()}").')
        super().visitEnumeration(ctx)
        self.parent_enum = None

    def visitBehavior(self, ctx: ModelParser.BehaviorContext):
        if ctx.name() is not None:
            self.behavior_name = ctx.name().getText()
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
        self.behavior_name = ':root'

    def visitFeature(self, ctx: ModelParser.FeatureContext):
        field: ModelParser.FieldContext = ctx.field()
        if field.number_def() is not None:
            type_name = 'num'
        elif field.string_def() is not None:
            type_name = 'text'
        else:
            # this seems hacky, I couldn't figure out how to do it better on the hurry
            try:
                type_name = field.type_ref().name().getText()
            except TypeError:
                type_name = ':root'
        feature_name = field.fieldName.getText()
        cardinality: ModelParser.CardinalityContext = ctx.cardinality()
        c_min = 1 if cardinality is None else cardinality.min
        c_max = 1 if cardinality is None else cardinality.max
        print(f'feature("{type_name}", "{feature_name}", {c_min}, {c_max}).')

    def visitAttribute(self, ctx: ModelParser.AttributeContext):
        if self.parent_enum is None:
            raise ValueError("illegal option")
        parent_name = self.parent_enum.name().getText()
        field: ModelParser.FieldContext = ctx.field()
        field_name = field.fieldName.getText()
        print(f'attribute("{parent_name}","{field_name}").')
        super().visitAttribute(ctx)

    def visitOption(self, ctx: ModelParser.OptionContext):
        if self.parent_enum is None:
            raise ValueError("illegal option")
        parent_name = self.parent_enum.name().getText()
        option_name = ctx.name().getText()
        print(f'option("{parent_name}", "{option_name}").')

        constant: ModelParser.ConstantContext = ctx.constant()
        if constant != []:
            parent_attr: ModelParser.AttributeContext = self.parent_enum.attribute(
            )
            for a, c in zip(parent_attr, constant):
                field: ModelParser.FieldContext = a.field()
                attr_name = field.fieldName.getText()
                if c.floating() is not None:
                    option_value = c.floating().getText()
                elif c.name() is not None:
                    option_value = f'"{c.name().getText()}"'
                print(
                    f'value("{parent_name}","{option_name}","{attr_name}",{option_value}).'
                )

    def visitConditioned(self, ctx: ModelParser.ConditionedContext):
        constraint_id = f'("{self.behavior_name}",{self.constraint_idx})'
        print(f'\nbehavior({constraint_id}).')
        super().visitConditioned(ctx)
        self.constraint_idx += 1

    def visitCombinations(self, ctx: ModelParser.CombinationsContext):
        constraint_id = f'("{self.behavior_name}",{self.constraint_idx})'
        for i, f in enumerate(ctx.formula()):
            print(f'combinations({constraint_id},{i},"{f.getText()}").')
        super().visitCombinations(ctx)
        self.row_idx = 0

    def visitCombination_row(self, ctx: ModelParser.Combination_rowContext):
        constraint_id = f'("{self.behavior_name}",{self.constraint_idx})'
        type = ctx.rowType.text
        for col_idx, item in enumerate(ctx.combination_item()):
            values = item.getText()
            # Removing brackets around the values. Is this safe?
            if ',' in values:
                values = values[1:-1]
            for v in values.split(','):
                print(
                    f'{type}({constraint_id},({col_idx},{self.row_idx}),"{v}").'
                )
        self.print_path = False
        super().visitCombination_row(ctx)
        self.print_path = True
        self.row_idx += 1

    def visitPrecondition(self, ctx: ModelParser.PreconditionContext):
        constraint_id = f'("{self.behavior_name}",{self.constraint_idx})'
        condition = f'"{ctx.condition().getText()}"'
        print(f'condition({constraint_id},{condition}).')
        super().visitPrecondition(ctx)

    def visitRequire(self, ctx: ModelParser.RequireContext):
        constraint_id = f'("{self.behavior_name}",{self.constraint_idx})'
        condition = f'"{ctx.condition().getText()}"'
        print(f'require({constraint_id},{condition}).')
        super().visitRequire(ctx)
        self.cond_idx = 0

    def visitCondition_or(self, ctx: ModelParser.Condition_orContext):
        cond_and: ModelParser.condition_andContext = ctx.condition_and()
        for i in range(len(cond_and) - 1):
            left = cond_and[i].getText()
            right = '||'.join([a.getText() for a in cond_and[i + 1:]])
            condition = left + '||' + right
            print(f'binary("{condition}","{left}","||","{right}").')
        super().visitCondition_or(ctx)

    def visitCondition_and(self, ctx: ModelParser.Condition_andContext):
        cond_not: ModelParser.condition_notContext = ctx.condition_not()
        for i in range(len(cond_not) - 1):
            left = cond_not[i].getText()
            right = '&&'.join([a.getText() for a in cond_not[i + 1:]])
            condition = left + '&&' + right
            print(f'binary("{condition}","{left}","&&","{right}").')
        super().visitCondition_and(ctx)

    def visitCondition_not(self, ctx: ModelParser.Condition_notContext):
        # TODO

        # cond_not: ModelParser.condition_notContext = ctx.condition_not()
        # if len(cond_not) > 1:
        #     for i in range(len(cond_not) - 1):
        #         left = cond_not[i].getText()
        #         right = '&&'.join([a.getText() for a in cond_not[i + 1:]])
        #         condition = left + '&&' + right
        #         print(f'binary("{condition}","{left}","&&","{right}").')
        super().visitCondition_not(ctx)

    def visitCondition_compare(self,
                               ctx: ModelParser.Condition_compareContext):
        formula: ModelParser.FormulaContext = ctx.formula()
        parts: ModelParser.Condition_partContext = ctx.condition_part()

        left = formula.getText()
        for i in range(len(parts)):
            # Binary atom for compare
            right = parts[i].formula().getText()
            compare = parts[i].compare().getText()
            condition = left + compare + right
            print(f'binary("{condition}","{left}","{compare}","{right}").')
            left = right

            # For multiple comparisons rewrite as propositional formulas connected by &&
            right_prop = '&&'.join([
                f'{l.formula().getText()}{r.getText()}'
                for l, r in (zip(parts[i:], parts[i + 1:]))
            ])
            if right_prop != '':
                complete_prop = condition + '&&' + right_prop
                print(
                    f'binary("{complete_prop}","{condition}","&&","{right_prop}").'
                )
        super().visitCondition_compare(ctx)

    def visitPath(self, ctx: ModelParser.PathContext):
        # Only do this for actual paths? Not formulas
        if self.print_path:
            full_path = f'"{ctx.getText()}"'
            for i, p in enumerate(ctx.path_item()):
                print(f'path({full_path},{i},"{p.getText()}").')

    # def visitFormula_atom(self, ctx: ModelParser.Formula_atomContext):
    #     print('\n')
    #     print(ctx.getText())
    #     if ctx.atom_path is not None:
    #         print(ctx.atom_path.getText())
    #     # print(ctx.atom_path)
    #     print(ctx.atom_num)
    #     print(ctx.atom_true)
    #     print(ctx.atom_false)
    #     # print(ctx.path().getText())
    #     super().visitFormula_atom(ctx)

    # def visitFormula(self, ctx: ModelParser.FormulaContext):
    #     print("formula")
    #     print(ctx.getText())
    #     print(ctx.formula_add().getText())
    #     # print(ctx.getText())
    #     # print(f'add().')
    #     super().visitFormula(ctx)

    # def visitFormula_add(self, ctx: ModelParser.Formula_addContext):
    #     print("add")
    #     formula = f'"{ctx.getText()}"'
    #     print(formula)
    #     for summand in ctx.formula_sub():
    #         print(summand.getText())
    #         # print(f'add({formula},"{self.behavior_name}"",{term1}).')
    #     super().visitFormula_add(ctx)

    # def visitFormula_sub(self, ctx: ModelParser.Formula_subContext):
    #     print("sub")
    #     print(ctx.getText())
    #     super().visitFormula_sub(ctx)

    # def visitFormula_mul(self, ctx: ModelParser.Formula_mulContext):
    #     print("mul")
    #     print(ctx.getText())
    #     super().visitFormula_mul(ctx)

    # def visitFormula_div(self, ctx: ModelParser.Formula_divContext):
    #     print("div")
    #     print(ctx.getText())
    #     super().visitFormula_div(ctx)

    # def visitFormula_pow(self, ctx: ModelParser.Formula_powContext):
    #     print("pow")
    #     print(ctx.getText())
    #     super().visitFormula_pow(ctx)

    # def visitFormula_func(self, ctx: ModelParser.Formula_funcContext):
    #     super().visitFormula_func(ctx)


if __name__ == "__main__":
    input_stream = FileStream(argv[1])
    lexer = ModelLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ModelParser(stream)
    tree = parser.root()
    visitor = ASPVisitor()
    visitor.visitRoot(tree)
