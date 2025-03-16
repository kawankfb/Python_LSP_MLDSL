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
        # Add preprocess keyword to symbol table
        self.symbol_table.insert(
            SymbolTable.Record(
                ctx.getChild(0).getText(),
                self.get_current_scope(),
                'keyword',
                None,
                None,
                ctx.getChild(0).symbol.line,
                ctx.getChild(0).symbol.column,
                len(ctx.getChild(0).getText())
            )
        )
        self.symbol_table.insert(
            SymbolTable.Record(
                ctx.getChild(1).getText(),
                self.get_current_scope(),
                'keyword',
                None,
                None,
                ctx.getChild(1).symbol.line,
                ctx.getChild(1).symbol.column,
                len(ctx.getChild(1).getText())
            )
        )

    def exitTrain(self, ctx):
        # Add preprocess keyword to symbol table
        self.symbol_table.insert(
            SymbolTable.Record(
                ctx.getChild(0).getText(),
                self.get_current_scope(),
                'keyword',
                None,
                None,
                ctx.getChild(0).symbol.line,
                ctx.getChild(0).symbol.column,
                len(ctx.getChild(0).getText())
            )
        )
        self.symbol_table.insert(
            SymbolTable.Record(
                ctx.getChild(1).getText(),
                self.get_current_scope(),
                'keyword',
                None,
                None,
                ctx.getChild(1).symbol.line,
                ctx.getChild(1).symbol.column,
                len(ctx.getChild(1).getText())
            )
        )

    def exitLoad(self, ctx):
        # Add preprocess keyword to symbol table
        self.symbol_table.insert(
            SymbolTable.Record(
                ctx.getChild(0).getText(),
                self.get_current_scope(),
                'keyword',
                None,
                None,
                ctx.getChild(0).symbol.line,
                ctx.getChild(0).symbol.column,
                len(ctx.getChild(0).getText())
            )
        )

    def exitLoad_dataset(self, ctx):
        # Add preprocess keyword to symbol table
        self.symbol_table.insert(
            SymbolTable.Record(
                ctx.getChild(0).getText(),
                self.get_current_scope(),
                'keyword',
                None,
                None,
                ctx.getChild(0).symbol.line,
                ctx.getChild(0).symbol.column,
                len(ctx.getChild(0).getText())
            )
        )


    def exitLoad_model(self, ctx):
        # Add preprocess keyword to symbol table
        self.symbol_table.insert(
            SymbolTable.Record(
                ctx.getChild(0).getText(),
                self.get_current_scope(),
                'keyword',
                None,
                None,
                ctx.getChild(0).symbol.line,
                ctx.getChild(0).symbol.column,
                len(ctx.getChild(0).getText())
            )
        )

    def exitSplit(self, ctx):
        # Add preprocess keyword to symbol table
        self.symbol_table.insert(
            SymbolTable.Record(
                ctx.getChild(0).getText(),
                self.get_current_scope(),
                'keyword',
                None,
                None,
                ctx.getChild(0).symbol.line,
                ctx.getChild(0).symbol.column,
                len(ctx.getChild(0).getText())
            )
        )
        self.symbol_table.insert(
            SymbolTable.Record(
                ctx.getChild(1).getText(),
                self.get_current_scope(),
                'keyword',
                None,
                None,
                ctx.getChild(1).symbol.line,
                ctx.getChild(1).symbol.column,
                len(ctx.getChild(1).getText())
            )
        )

    def exitEvaluate(self, ctx):
        # Add preprocess keyword to symbol table
        self.symbol_table.insert(
            SymbolTable.Record(
                ctx.getChild(0).getText(),
                self.get_current_scope(),
                'keyword',
                None,
                None,
                ctx.getChild(0).symbol.line,
                ctx.getChild(0).symbol.column,
                len(ctx.getChild(0).getText())
            )
        )
        self.symbol_table.insert(
            SymbolTable.Record(
                ctx.getChild(1).getText(),
                self.get_current_scope(),
                'keyword',
                None,
                None,
                ctx.getChild(1).symbol.line,
                ctx.getChild(1).symbol.column,
                len(ctx.getChild(1).getText())
            )
        )


    def exitId(self, ctx:MLDSLParser.IdContext):
        self.symbol_table.insert(
            SymbolTable.Record(
                ctx.getChild(0).getText(),
                self.get_current_scope(),
                'property',
                None,
                None,
                ctx.getChild(0).symbol.line,
                ctx.getChild(0).symbol.column,
                len(ctx.getChild(0).getText())
            )
        )

    def exitString(self, ctx:MLDSLParser.StringContext):
        self.symbol_table.insert(
            SymbolTable.Record(
                ctx.getChild(0).getText(),
                self.get_current_scope(),
                'string',
                None,
                None,
                ctx.getChild(0).symbol.line,
                ctx.getChild(0).symbol.column,
                len(ctx.getChild(0).getText())
            )
        )

    def exitParameter(self, ctx:MLDSLParser.ParameterContext):
        self.symbol_table.insert(
            SymbolTable.Record(
                ctx.getText(),
                self.get_current_scope(),
                'parameter',
                None,
                None,
                ctx.getChild(0).getChild(0).symbol.line,
                ctx.getChild(0).getChild(0).symbol.column,
                len(ctx.getChild(0).getText())
            )
        )

    def exitPython_code(self, ctx:MLDSLParser.Python_codeContext):
        # Add preprocess keyword to symbol table
        self.symbol_table.insert(
            SymbolTable.Record(
                "@py_start",
                self.get_current_scope(),
                'decorator',
                None,
                None,
                ctx.getChild(0).symbol.line,
                ctx.getChild(0).symbol.column,
                9
            )
        )
        new_lines_count = ctx.getChild(0).getText().count('\n')
        self.symbol_table.insert(
            SymbolTable.Record(
                "@py_end",
                self.get_current_scope(),
                'decorator',
                None,
                None,
                ctx.getChild(0).symbol.line+ new_lines_count,
                0,
                7
            )
        )
