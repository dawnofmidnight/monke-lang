from parser import *
from monke_parser import *
from monke_ast import *


class Compiler:
    def __init__(self, ast):
        self.ast = ast

    def compile(self, main_ast=None):
        if main_ast is None:
            main_ast = self.ast

        code = []
        constant_table = []

        for ast in main_ast:
            if isinstance(ast, FunctionCall):
                if ast.name == "chatter":
                    for argument in ast.arguments:
                        constant_table.append(argument.value)
                        index = constant_table.index(argument.value)

                        code.append(("LOAD_VALUE", index))

                    code.append(("PRINT_VALUE", 0))

            if ast == Expr:
                code.append(argument.value)
                index = constant_table.index(argument.value)

                code.append(("LOAD_VALUE", index))

        return code, constant_table
