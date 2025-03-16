from antlr4 import *

from mldslls.dslf_language_helpers.MLDSLSemanticTokenListener import MLDSLSemanticListener
from mldslls.dslf_language_helpers.gen.MLDSLLexer import MLDSLLexer
from mldslls.dslf_language_helpers.gen.MLDSLParser import MLDSLParser
from mldslls.dslf_language_helpers.symbol_table import SymbolTable

def get_token_type_id_from_record_type(type):
    type_to_id_mapper = {
        "keyword": 0,
        "string": 1,
        "property":2,
        "parameter":3,
        "comment":4,
        "decorator":5
    }
    return type_to_id_mapper[type]

def get_semantic_token_data(uri='file:///d%3A/PhD/Projects/Languages/MLDSL/MLDSL_Example/test_st_1.mlc'):
    stream = FileStream(uri, encoding='utf8')
    lexer = MLDSLLexer(stream)
    token_stream = CommonTokenStream(lexer)
    parser = MLDSLParser(token_stream)
    parse_tree = parser.program()
    symbol_table = SymbolTable()
    semantic_token_listener = MLDSLSemanticListener(symbol_table,parser.ruleNames)
    walker = ParseTreeWalker()

    for token in token_stream.tokens:
        if token.type == MLDSLLexer.COMMENT:
            comment = token
            symbol_table.insert(
            SymbolTable.Record(
                comment.text,
                "",
                'comment',
                None,
                None,
                comment.line,
                comment.column,
                len(comment.text)
            )
        )

    walker.walk(t=parse_tree, listener=semantic_token_listener)
    semantic_token_data = []


    last_token_line = 0
    last_token_offset =0
    sorted_list = sorted(symbol_table.table,key=lambda x: (x.record_line, x.record_offset))
    for record in sorted_list:
        semantic_token_data.append(record.record_line-1-last_token_line)
        semantic_token_data.append(record.record_offset-last_token_offset if last_token_line == record.record_line-1 else record.record_offset)
        semantic_token_data.append(record.record_length)
        semantic_token_data.append(get_token_type_id_from_record_type(record.record_type))
        semantic_token_data.append(0) # should be modifier
        last_token_line = record.record_line-1
        last_token_offset = record.record_offset

    return semantic_token_data


