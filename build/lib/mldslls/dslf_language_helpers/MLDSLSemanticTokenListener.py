from antlr4 import *

from mldslls.dslf_language_helpers.gen.MLDSLListener import MLDSLListener
from mldslls.dslf_language_helpers.symbol_table import SymbolTable
from mldslls.dslf_language_helpers.gen.MLDSLParser import MLDSLParser

class MLDSLSemanticListener(MLDSLListener):
    def __init__(self,symbol_table,rule_names):
        self.scoped_operators = ['if', 'for', 'while', 'block']
        self.symbol_table: SymbolTable = symbol_table
        self.current_scope_stack = []
        self.scoped_rules = ['compoundst', 'ifst', 'whilest', 'case', 'forst']
        self.rule_names = rule_names
        self.scope_identifier_dictionary = dict()

    def get_scope_convention(self, last_rule_name):
        res = ""
        for entry in self.current_scope_stack:
            res = res + entry + "_"
        return res + last_rule_name

    def get_current_scope(self):
        return self.get_scope_convention("").removesuffix("_")

    # Exit a parse tree produced by MLDSLParser#preprocess.
    def exitPreprocess(self, ctx:MLDSLParser.PreprocessContext):
        self.symbol_table.insert(
            SymbolTable.Record(
                ctx.getChild(0).getText(),
                self.get_current_scope(),
                'integer',
                5,
                None,
                ctx.getChild(0).symbol.line,
                ctx.getChild(0).symbol.column,
                len(ctx.getChild(0).getText())
            )
        )