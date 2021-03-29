from monke_ast import FunctionCall
import sys
from lexer import Lexer
from monke_ast import *


class MonkeParser:
    def __init__(self, string_input):
        self.string_input = string_input

        self.lexer = Lexer(string_input)

        self.lexer.lex()

    def parse(self):
        ast = []

        for token in self.lexer.tokens:
            current_token = self.lexer.next()

            if self.lexer.current_token.type == "CHATTER":
                if self.lexer.peek().type == "LBRACE":
                    arguments = []
                    while current_token.type != "RBRACE":
                        current_token = self.lexer.next()

                        if current_token.type == "INTEGER":
                            integer = Expr(int(current_token.text))

                            arguments.append(integer)

                        elif current_token.type in ("DOUBLEQUOTEDSTRING", "SINGLEQUOTEDSTRING"):
                            string = Expr(str(current_token.text).replace(
                                '"', "").replace("'", ""))

                            arguments.append(string)
                else:
                    for token in self.lexer.tokens:
                        print(token.type)
                    print(current_token.text)
                    sys.stderr.write(
                        f"Invalid Syntax; expected '(', found {self.lexer.peek().text}")
                    sys.exit(1)

                chatter = FunctionCall("chatter", arguments)

                ast.append(chatter)

            elif self.lexer.current_token.type == "EOF":
                break

        return ast
