from parser import *
from monke_parser import *
from monke_ast import *


class Compiler:
    """
    This is the monkelang's default Compiler class. This class takes an AST and
    generates opcodes by walking it. An AST can be provided to the compile
    method if the ast provided in the initialization of the class is not
    wanted.
    """
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
                        if isinstance(argument, Expr):
                            constant_table.append(argument.value)
                            index = constant_table.index(argument.value)

                            code.append(("LOAD_VALUE", index))

                        elif isinstance(argument, BinOp):
                            constant_table.append(argument.rhs.value)

                            index = constant_table.index(argument.rhs.value)
                            code.append(("LOAD_VALUE", index))

                            constant_table.append(argument.lhs.value)
                            index = constant_table.index(argument.lhs.value)
                            code.append(("LOAD_VALUE", index))

                            if argument.op == "+":
                                code.append(("ADD_TWO_VALUES", 0))
                            elif argument.op == "-":
                                code.append(("SUB_TWO_VALUES", 0))
                            if argument.op == "*":
                                code.append(("MUL_TWO_VALUES", 0))
                            elif argument.op == "/":
                                code.append(("DIV_TWO_VALUES", 0))

                    code.append(("PRINT_VALUE", 0))

            if isinstance(ast, Expr):
                code.append(argument.value)
                index = constant_table.index(argument.value)

                code.append(("LOAD_VALUE", index))

            elif isinstance(ast, BinOp):
                constant_table.append(argument.rhs.value)

                index = constant_table.index(argument.rhs.value)
                code.append(("LOAD_VALUE", index))

                constant_table.append(argument.lhs.value)
                index = constant_table.index(argument.lhs.value)
                code.append(("LOAD_VALUE", index))

                if argument.op == "+":
                    code.append(("ADD_TWO_VALUES", 0))
                elif argument.op == "-":
                    code.append(("SUB_TWO_VALUES", 0))
                if argument.op == "*":
                    code.append(("MUL_TWO_VALUES", 0))
                elif argument.op == "/":
                    code.append(("DIV_TWO_VALUES", 0))

        return code, constant_table
