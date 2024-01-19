// Generated from /home/nruehling/projects/coom-encoding/model/Model.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link ModelParser}.
 */
public interface ModelListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link ModelParser#root}.
	 * @param ctx the parse tree
	 */
	void enterRoot(ModelParser.RootContext ctx);
	/**
	 * Exit a parse tree produced by {@link ModelParser#root}.
	 * @param ctx the parse tree
	 */
	void exitRoot(ModelParser.RootContext ctx);
	/**
	 * Enter a parse tree produced by {@link ModelParser#product}.
	 * @param ctx the parse tree
	 */
	void enterProduct(ModelParser.ProductContext ctx);
	/**
	 * Exit a parse tree produced by {@link ModelParser#product}.
	 * @param ctx the parse tree
	 */
	void exitProduct(ModelParser.ProductContext ctx);
	/**
	 * Enter a parse tree produced by {@link ModelParser#structure}.
	 * @param ctx the parse tree
	 */
	void enterStructure(ModelParser.StructureContext ctx);
	/**
	 * Exit a parse tree produced by {@link ModelParser#structure}.
	 * @param ctx the parse tree
	 */
	void exitStructure(ModelParser.StructureContext ctx);
	/**
	 * Enter a parse tree produced by {@link ModelParser#enumeration}.
	 * @param ctx the parse tree
	 */
	void enterEnumeration(ModelParser.EnumerationContext ctx);
	/**
	 * Exit a parse tree produced by {@link ModelParser#enumeration}.
	 * @param ctx the parse tree
	 */
	void exitEnumeration(ModelParser.EnumerationContext ctx);
	/**
	 * Enter a parse tree produced by {@link ModelParser#behavior}.
	 * @param ctx the parse tree
	 */
	void enterBehavior(ModelParser.BehaviorContext ctx);
	/**
	 * Exit a parse tree produced by {@link ModelParser#behavior}.
	 * @param ctx the parse tree
	 */
	void exitBehavior(ModelParser.BehaviorContext ctx);
	/**
	 * Enter a parse tree produced by {@link ModelParser#behavior_block}.
	 * @param ctx the parse tree
	 */
	void enterBehavior_block(ModelParser.Behavior_blockContext ctx);
	/**
	 * Exit a parse tree produced by {@link ModelParser#behavior_block}.
	 * @param ctx the parse tree
	 */
	void exitBehavior_block(ModelParser.Behavior_blockContext ctx);
	/**
	 * Enter a parse tree produced by {@link ModelParser#feature}.
	 * @param ctx the parse tree
	 */
	void enterFeature(ModelParser.FeatureContext ctx);
	/**
	 * Exit a parse tree produced by {@link ModelParser#feature}.
	 * @param ctx the parse tree
	 */
	void exitFeature(ModelParser.FeatureContext ctx);
	/**
	 * Enter a parse tree produced by {@link ModelParser#cardinality}.
	 * @param ctx the parse tree
	 */
	void enterCardinality(ModelParser.CardinalityContext ctx);
	/**
	 * Exit a parse tree produced by {@link ModelParser#cardinality}.
	 * @param ctx the parse tree
	 */
	void exitCardinality(ModelParser.CardinalityContext ctx);
	/**
	 * Enter a parse tree produced by {@link ModelParser#attribute}.
	 * @param ctx the parse tree
	 */
	void enterAttribute(ModelParser.AttributeContext ctx);
	/**
	 * Exit a parse tree produced by {@link ModelParser#attribute}.
	 * @param ctx the parse tree
	 */
	void exitAttribute(ModelParser.AttributeContext ctx);
	/**
	 * Enter a parse tree produced by {@link ModelParser#option}.
	 * @param ctx the parse tree
	 */
	void enterOption(ModelParser.OptionContext ctx);
	/**
	 * Exit a parse tree produced by {@link ModelParser#option}.
	 * @param ctx the parse tree
	 */
	void exitOption(ModelParser.OptionContext ctx);
	/**
	 * Enter a parse tree produced by {@link ModelParser#field}.
	 * @param ctx the parse tree
	 */
	void enterField(ModelParser.FieldContext ctx);
	/**
	 * Exit a parse tree produced by {@link ModelParser#field}.
	 * @param ctx the parse tree
	 */
	void exitField(ModelParser.FieldContext ctx);
	/**
	 * Enter a parse tree produced by {@link ModelParser#number_def}.
	 * @param ctx the parse tree
	 */
	void enterNumber_def(ModelParser.Number_defContext ctx);
	/**
	 * Exit a parse tree produced by {@link ModelParser#number_def}.
	 * @param ctx the parse tree
	 */
	void exitNumber_def(ModelParser.Number_defContext ctx);
	/**
	 * Enter a parse tree produced by {@link ModelParser#string_def}.
	 * @param ctx the parse tree
	 */
	void enterString_def(ModelParser.String_defContext ctx);
	/**
	 * Exit a parse tree produced by {@link ModelParser#string_def}.
	 * @param ctx the parse tree
	 */
	void exitString_def(ModelParser.String_defContext ctx);
	/**
	 * Enter a parse tree produced by {@link ModelParser#define}.
	 * @param ctx the parse tree
	 */
	void enterDefine(ModelParser.DefineContext ctx);
	/**
	 * Exit a parse tree produced by {@link ModelParser#define}.
	 * @param ctx the parse tree
	 */
	void exitDefine(ModelParser.DefineContext ctx);
	/**
	 * Enter a parse tree produced by {@link ModelParser#conditioned}.
	 * @param ctx the parse tree
	 */
	void enterConditioned(ModelParser.ConditionedContext ctx);
	/**
	 * Exit a parse tree produced by {@link ModelParser#conditioned}.
	 * @param ctx the parse tree
	 */
	void exitConditioned(ModelParser.ConditionedContext ctx);
	/**
	 * Enter a parse tree produced by {@link ModelParser#combinations}.
	 * @param ctx the parse tree
	 */
	void enterCombinations(ModelParser.CombinationsContext ctx);
	/**
	 * Exit a parse tree produced by {@link ModelParser#combinations}.
	 * @param ctx the parse tree
	 */
	void exitCombinations(ModelParser.CombinationsContext ctx);
	/**
	 * Enter a parse tree produced by {@link ModelParser#explanation}.
	 * @param ctx the parse tree
	 */
	void enterExplanation(ModelParser.ExplanationContext ctx);
	/**
	 * Exit a parse tree produced by {@link ModelParser#explanation}.
	 * @param ctx the parse tree
	 */
	void exitExplanation(ModelParser.ExplanationContext ctx);
	/**
	 * Enter a parse tree produced by {@link ModelParser#index_quantification}.
	 * @param ctx the parse tree
	 */
	void enterIndex_quantification(ModelParser.Index_quantificationContext ctx);
	/**
	 * Exit a parse tree produced by {@link ModelParser#index_quantification}.
	 * @param ctx the parse tree
	 */
	void exitIndex_quantification(ModelParser.Index_quantificationContext ctx);
	/**
	 * Enter a parse tree produced by {@link ModelParser#precondition}.
	 * @param ctx the parse tree
	 */
	void enterPrecondition(ModelParser.PreconditionContext ctx);
	/**
	 * Exit a parse tree produced by {@link ModelParser#precondition}.
	 * @param ctx the parse tree
	 */
	void exitPrecondition(ModelParser.PreconditionContext ctx);
	/**
	 * Enter a parse tree produced by {@link ModelParser#assign_default}.
	 * @param ctx the parse tree
	 */
	void enterAssign_default(ModelParser.Assign_defaultContext ctx);
	/**
	 * Exit a parse tree produced by {@link ModelParser#assign_default}.
	 * @param ctx the parse tree
	 */
	void exitAssign_default(ModelParser.Assign_defaultContext ctx);
	/**
	 * Enter a parse tree produced by {@link ModelParser#assign_imply}.
	 * @param ctx the parse tree
	 */
	void enterAssign_imply(ModelParser.Assign_implyContext ctx);
	/**
	 * Exit a parse tree produced by {@link ModelParser#assign_imply}.
	 * @param ctx the parse tree
	 */
	void exitAssign_imply(ModelParser.Assign_implyContext ctx);
	/**
	 * Enter a parse tree produced by {@link ModelParser#assign_new}.
	 * @param ctx the parse tree
	 */
	void enterAssign_new(ModelParser.Assign_newContext ctx);
	/**
	 * Exit a parse tree produced by {@link ModelParser#assign_new}.
	 * @param ctx the parse tree
	 */
	void exitAssign_new(ModelParser.Assign_newContext ctx);
	/**
	 * Enter a parse tree produced by {@link ModelParser#interaction}.
	 * @param ctx the parse tree
	 */
	void enterInteraction(ModelParser.InteractionContext ctx);
	/**
	 * Exit a parse tree produced by {@link ModelParser#interaction}.
	 * @param ctx the parse tree
	 */
	void exitInteraction(ModelParser.InteractionContext ctx);
	/**
	 * Enter a parse tree produced by {@link ModelParser#message}.
	 * @param ctx the parse tree
	 */
	void enterMessage(ModelParser.MessageContext ctx);
	/**
	 * Exit a parse tree produced by {@link ModelParser#message}.
	 * @param ctx the parse tree
	 */
	void exitMessage(ModelParser.MessageContext ctx);
	/**
	 * Enter a parse tree produced by {@link ModelParser#require}.
	 * @param ctx the parse tree
	 */
	void enterRequire(ModelParser.RequireContext ctx);
	/**
	 * Exit a parse tree produced by {@link ModelParser#require}.
	 * @param ctx the parse tree
	 */
	void exitRequire(ModelParser.RequireContext ctx);
	/**
	 * Enter a parse tree produced by {@link ModelParser#prefer}.
	 * @param ctx the parse tree
	 */
	void enterPrefer(ModelParser.PreferContext ctx);
	/**
	 * Exit a parse tree produced by {@link ModelParser#prefer}.
	 * @param ctx the parse tree
	 */
	void exitPrefer(ModelParser.PreferContext ctx);
	/**
	 * Enter a parse tree produced by {@link ModelParser#combination_row}.
	 * @param ctx the parse tree
	 */
	void enterCombination_row(ModelParser.Combination_rowContext ctx);
	/**
	 * Exit a parse tree produced by {@link ModelParser#combination_row}.
	 * @param ctx the parse tree
	 */
	void exitCombination_row(ModelParser.Combination_rowContext ctx);
	/**
	 * Enter a parse tree produced by {@link ModelParser#combination_item}.
	 * @param ctx the parse tree
	 */
	void enterCombination_item(ModelParser.Combination_itemContext ctx);
	/**
	 * Exit a parse tree produced by {@link ModelParser#combination_item}.
	 * @param ctx the parse tree
	 */
	void exitCombination_item(ModelParser.Combination_itemContext ctx);
	/**
	 * Enter a parse tree produced by {@link ModelParser#combination_atom}.
	 * @param ctx the parse tree
	 */
	void enterCombination_atom(ModelParser.Combination_atomContext ctx);
	/**
	 * Exit a parse tree produced by {@link ModelParser#combination_atom}.
	 * @param ctx the parse tree
	 */
	void exitCombination_atom(ModelParser.Combination_atomContext ctx);
	/**
	 * Enter a parse tree produced by {@link ModelParser#stmt_end}.
	 * @param ctx the parse tree
	 */
	void enterStmt_end(ModelParser.Stmt_endContext ctx);
	/**
	 * Exit a parse tree produced by {@link ModelParser#stmt_end}.
	 * @param ctx the parse tree
	 */
	void exitStmt_end(ModelParser.Stmt_endContext ctx);
	/**
	 * Enter a parse tree produced by {@link ModelParser#constant}.
	 * @param ctx the parse tree
	 */
	void enterConstant(ModelParser.ConstantContext ctx);
	/**
	 * Exit a parse tree produced by {@link ModelParser#constant}.
	 * @param ctx the parse tree
	 */
	void exitConstant(ModelParser.ConstantContext ctx);
	/**
	 * Enter a parse tree produced by {@link ModelParser#floating}.
	 * @param ctx the parse tree
	 */
	void enterFloating(ModelParser.FloatingContext ctx);
	/**
	 * Exit a parse tree produced by {@link ModelParser#floating}.
	 * @param ctx the parse tree
	 */
	void exitFloating(ModelParser.FloatingContext ctx);
	/**
	 * Enter a parse tree produced by {@link ModelParser#compare}.
	 * @param ctx the parse tree
	 */
	void enterCompare(ModelParser.CompareContext ctx);
	/**
	 * Exit a parse tree produced by {@link ModelParser#compare}.
	 * @param ctx the parse tree
	 */
	void exitCompare(ModelParser.CompareContext ctx);
	/**
	 * Enter a parse tree produced by {@link ModelParser#unit}.
	 * @param ctx the parse tree
	 */
	void enterUnit(ModelParser.UnitContext ctx);
	/**
	 * Exit a parse tree produced by {@link ModelParser#unit}.
	 * @param ctx the parse tree
	 */
	void exitUnit(ModelParser.UnitContext ctx);
	/**
	 * Enter a parse tree produced by {@link ModelParser#fraction}.
	 * @param ctx the parse tree
	 */
	void enterFraction(ModelParser.FractionContext ctx);
	/**
	 * Exit a parse tree produced by {@link ModelParser#fraction}.
	 * @param ctx the parse tree
	 */
	void exitFraction(ModelParser.FractionContext ctx);
	/**
	 * Enter a parse tree produced by {@link ModelParser#path}.
	 * @param ctx the parse tree
	 */
	void enterPath(ModelParser.PathContext ctx);
	/**
	 * Exit a parse tree produced by {@link ModelParser#path}.
	 * @param ctx the parse tree
	 */
	void exitPath(ModelParser.PathContext ctx);
	/**
	 * Enter a parse tree produced by {@link ModelParser#path_item}.
	 * @param ctx the parse tree
	 */
	void enterPath_item(ModelParser.Path_itemContext ctx);
	/**
	 * Exit a parse tree produced by {@link ModelParser#path_item}.
	 * @param ctx the parse tree
	 */
	void exitPath_item(ModelParser.Path_itemContext ctx);
	/**
	 * Enter a parse tree produced by {@link ModelParser#path_index}.
	 * @param ctx the parse tree
	 */
	void enterPath_index(ModelParser.Path_indexContext ctx);
	/**
	 * Exit a parse tree produced by {@link ModelParser#path_index}.
	 * @param ctx the parse tree
	 */
	void exitPath_index(ModelParser.Path_indexContext ctx);
	/**
	 * Enter a parse tree produced by {@link ModelParser#condition}.
	 * @param ctx the parse tree
	 */
	void enterCondition(ModelParser.ConditionContext ctx);
	/**
	 * Exit a parse tree produced by {@link ModelParser#condition}.
	 * @param ctx the parse tree
	 */
	void exitCondition(ModelParser.ConditionContext ctx);
	/**
	 * Enter a parse tree produced by {@link ModelParser#condition_or}.
	 * @param ctx the parse tree
	 */
	void enterCondition_or(ModelParser.Condition_orContext ctx);
	/**
	 * Exit a parse tree produced by {@link ModelParser#condition_or}.
	 * @param ctx the parse tree
	 */
	void exitCondition_or(ModelParser.Condition_orContext ctx);
	/**
	 * Enter a parse tree produced by {@link ModelParser#condition_and}.
	 * @param ctx the parse tree
	 */
	void enterCondition_and(ModelParser.Condition_andContext ctx);
	/**
	 * Exit a parse tree produced by {@link ModelParser#condition_and}.
	 * @param ctx the parse tree
	 */
	void exitCondition_and(ModelParser.Condition_andContext ctx);
	/**
	 * Enter a parse tree produced by {@link ModelParser#condition_not}.
	 * @param ctx the parse tree
	 */
	void enterCondition_not(ModelParser.Condition_notContext ctx);
	/**
	 * Exit a parse tree produced by {@link ModelParser#condition_not}.
	 * @param ctx the parse tree
	 */
	void exitCondition_not(ModelParser.Condition_notContext ctx);
	/**
	 * Enter a parse tree produced by {@link ModelParser#condition_compare}.
	 * @param ctx the parse tree
	 */
	void enterCondition_compare(ModelParser.Condition_compareContext ctx);
	/**
	 * Exit a parse tree produced by {@link ModelParser#condition_compare}.
	 * @param ctx the parse tree
	 */
	void exitCondition_compare(ModelParser.Condition_compareContext ctx);
	/**
	 * Enter a parse tree produced by {@link ModelParser#condition_part}.
	 * @param ctx the parse tree
	 */
	void enterCondition_part(ModelParser.Condition_partContext ctx);
	/**
	 * Exit a parse tree produced by {@link ModelParser#condition_part}.
	 * @param ctx the parse tree
	 */
	void exitCondition_part(ModelParser.Condition_partContext ctx);
	/**
	 * Enter a parse tree produced by {@link ModelParser#formula}.
	 * @param ctx the parse tree
	 */
	void enterFormula(ModelParser.FormulaContext ctx);
	/**
	 * Exit a parse tree produced by {@link ModelParser#formula}.
	 * @param ctx the parse tree
	 */
	void exitFormula(ModelParser.FormulaContext ctx);
	/**
	 * Enter a parse tree produced by {@link ModelParser#formula_add}.
	 * @param ctx the parse tree
	 */
	void enterFormula_add(ModelParser.Formula_addContext ctx);
	/**
	 * Exit a parse tree produced by {@link ModelParser#formula_add}.
	 * @param ctx the parse tree
	 */
	void exitFormula_add(ModelParser.Formula_addContext ctx);
	/**
	 * Enter a parse tree produced by {@link ModelParser#formula_sub}.
	 * @param ctx the parse tree
	 */
	void enterFormula_sub(ModelParser.Formula_subContext ctx);
	/**
	 * Exit a parse tree produced by {@link ModelParser#formula_sub}.
	 * @param ctx the parse tree
	 */
	void exitFormula_sub(ModelParser.Formula_subContext ctx);
	/**
	 * Enter a parse tree produced by {@link ModelParser#formula_mul}.
	 * @param ctx the parse tree
	 */
	void enterFormula_mul(ModelParser.Formula_mulContext ctx);
	/**
	 * Exit a parse tree produced by {@link ModelParser#formula_mul}.
	 * @param ctx the parse tree
	 */
	void exitFormula_mul(ModelParser.Formula_mulContext ctx);
	/**
	 * Enter a parse tree produced by {@link ModelParser#formula_div}.
	 * @param ctx the parse tree
	 */
	void enterFormula_div(ModelParser.Formula_divContext ctx);
	/**
	 * Exit a parse tree produced by {@link ModelParser#formula_div}.
	 * @param ctx the parse tree
	 */
	void exitFormula_div(ModelParser.Formula_divContext ctx);
	/**
	 * Enter a parse tree produced by {@link ModelParser#formula_pow}.
	 * @param ctx the parse tree
	 */
	void enterFormula_pow(ModelParser.Formula_powContext ctx);
	/**
	 * Exit a parse tree produced by {@link ModelParser#formula_pow}.
	 * @param ctx the parse tree
	 */
	void exitFormula_pow(ModelParser.Formula_powContext ctx);
	/**
	 * Enter a parse tree produced by {@link ModelParser#formula_sign}.
	 * @param ctx the parse tree
	 */
	void enterFormula_sign(ModelParser.Formula_signContext ctx);
	/**
	 * Exit a parse tree produced by {@link ModelParser#formula_sign}.
	 * @param ctx the parse tree
	 */
	void exitFormula_sign(ModelParser.Formula_signContext ctx);
	/**
	 * Enter a parse tree produced by {@link ModelParser#formula_func}.
	 * @param ctx the parse tree
	 */
	void enterFormula_func(ModelParser.Formula_funcContext ctx);
	/**
	 * Exit a parse tree produced by {@link ModelParser#formula_func}.
	 * @param ctx the parse tree
	 */
	void exitFormula_func(ModelParser.Formula_funcContext ctx);
	/**
	 * Enter a parse tree produced by {@link ModelParser#formula_atom}.
	 * @param ctx the parse tree
	 */
	void enterFormula_atom(ModelParser.Formula_atomContext ctx);
	/**
	 * Exit a parse tree produced by {@link ModelParser#formula_atom}.
	 * @param ctx the parse tree
	 */
	void exitFormula_atom(ModelParser.Formula_atomContext ctx);
	/**
	 * Enter a parse tree produced by {@link ModelParser#name}.
	 * @param ctx the parse tree
	 */
	void enterName(ModelParser.NameContext ctx);
	/**
	 * Exit a parse tree produced by {@link ModelParser#name}.
	 * @param ctx the parse tree
	 */
	void exitName(ModelParser.NameContext ctx);
	/**
	 * Enter a parse tree produced by {@link ModelParser#date}.
	 * @param ctx the parse tree
	 */
	void enterDate(ModelParser.DateContext ctx);
	/**
	 * Exit a parse tree produced by {@link ModelParser#date}.
	 * @param ctx the parse tree
	 */
	void exitDate(ModelParser.DateContext ctx);
}