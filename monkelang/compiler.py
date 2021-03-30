from monke_parser import *
from monke_ast import *

import sys


class Compiler:
    """
    This is the monkelang's default Compiler class. This class takes an AST and
    generates opself.codes by walking it. An AST can be provided to the compile
    method if the ast provided in the initialization of the class is not
    wanted.
    """

    def __init__(self, ast, vm):
        self.ast = ast
        self.vm = vm
        
        self.code = []
        self.constant_table = []

        self.locals = {}

    def compile(self, main_ast=None):
        if main_ast is None:
            main_ast = self.ast

        self.constant_table = []

        for ast in main_ast:
            if isinstance(ast, FunctionCall):
                if ast.name == "chatter":
                    for argument in ast.arguments:
                        if isinstance(argument, Expr):
                            self.constant_table.append(argument.value)
                            index = self.constant_table.index(argument.value)

                            self.code.append(("LOAD_VALUE", index))

                        elif isinstance(argument, BinOp):
                            self.constant_table.append(argument.rhs.value)

                            index = self.constant_table.index(argument.rhs.value)
                            self.code.append(("LOAD_VALUE", index))

                            self.constant_table.append(argument.lhs.value)
                            index = self.constant_table.index(argument.lhs.value)
                            self.code.append(("LOAD_VALUE", index))

                            if argument.op == "+":
                                self.code.append(("ADD_TWO_VALUES", 0))
                            elif argument.op == "-":
                                self.code.append(("SUB_TWO_VALUES", 0))
                            if argument.op == "*":
                                self.code.append(("MUL_TWO_VALUES", 0))
                            elif argument.op == "/":
                                self.code.append(("DIV_TWO_VALUES", 0))

                        elif isinstance(argument, VariableExpr):
                            try:
                                depth = self.locals[argument.name]
                            except KeyError:
                                sys.stderr.write(
                                    f"InvalidIdentifier: No variable/identifier called {argument.name}")
                                sys.exit(1)

                            self.code.append(("GET_LOCAL", depth))

                    self.code.append(("PRINT_VALUE", 0))

            elif isinstance(ast, Expr):
                self.constant_table.append(ast.value)
                index = self.constant_table.index(ast.value)

                self.code.append(("LOAD_VALUE", index))

            elif isinstance(ast, BinOp):
                self.constant_table.append(ast.rhs.value)

                index = self.constant_table.index(ast.rhs.value)
                self.code.append(("LOAD_VALUE", index))

                self.constant_table.append(ast.lhs.value)
                index = self.constant_table.index(ast.lhs.value)
                self.code.append(("LOAD_VALUE", index))

                if ast.op == "+":
                    self.code.append(("ADD_TWO_VALUES", 0))
                elif ast.op == "-":
                    self.code.append(("SUB_TWO_VALUES", 0))
                if ast.op == "*":
                    self.code.append(("MUL_TWO_VALUES", 0))
                elif ast.op == "/":
                    self.code.append(("DIV_TWO_VALUES", 0))

            elif isinstance(ast, AssignmentExpr):
                self.compile([ast.value])

                index = len(self.vm.stack) + 1

                self.locals[ast.name] = index

                self.code.append(("SET_LOCAL", index))

        return self.code, self.constant_table
