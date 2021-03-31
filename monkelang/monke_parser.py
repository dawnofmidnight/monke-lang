from monke_ast import FunctionCall
import sys
from lexer import Lexer
from monke_ast import *


class MonkeParser:
    """
    This is the monkelang default parser. This class takes a string input
    and lexes them into tokens using the Lexer class. The parser then
    iterates through the tokens to generate an AST (Abstract Syntax Tree).
    """

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

                        elif current_token.type == "PLUS":
                            lhs = self.lexer.tokens[self.lexer.token_pos - 1]

                            arguments.pop()

                            rhs = self.lexer.next()

                            if lhs.type == "INTEGER":
                                if rhs.type == "INTEGER":
                                    binop = BinOp(
                                        Expr(int(lhs.text)), Expr(int(rhs.text)), "+")

                                    arguments.append(binop)
                                elif rhs.type in ("DOUBLEQUOTEDSTRING", "SINGLEQUOTEDSTRING"):
                                    sys.stderr.write(
                                        f"InvalidTypeError: Cannot add INTEGER {lhs.text} to STRING {rhs.text}")
                                    sys.exit(1)
                            elif lhs.type in ("DOUBLEQUOTEDSTRING", "SINGLEQUOTEDSTRING"):
                                if rhs.type in ("DOUBLEQUOTEDSTRING", "SINGLEQUOTEDSTRING"):
                                    binop = BinOp(Expr(str(lhs.text.replace('"', "").replace("'", ""))), Expr(
                                        str(rhs.text).replace('"', "").replace("'", "")), "+")

                                    arguments.append(binop)
                                elif rhs.type == "INTEGER":
                                    sys.stderr.write(
                                        f"InvalidTypeError: Cannot add STRING {lhs.text} to INTEGER {rhs.text}")
                                    sys.exit(1)

                        elif current_token.type == "MINUS":
                            lhs = self.lexer.tokens[self.lexer.token_pos - 1]

                            arguments.pop()

                            rhs = self.lexer.next()

                            if lhs.type == "INTEGER":
                                if rhs.type == "INTEGER":
                                    binop = BinOp(
                                        Expr(int(lhs.text)), Expr(
                                            int(rhs.text)), "-"
                                    )

                                    arguments.append(binop)
                                elif rhs.type in ("DOUBLEQUOTEDSTRING", "SINGLEQUOTEDSTRING"):
                                    sys.stderr.write(
                                        f"Cannot subbtract STRING {rhs.text} from INTEGER {lhs.text}")
                                    sys.exit(1)
                            elif lhs.type == "STRING":
                                sys.stderr.write(
                                    f"Cannot subtract using STRING {lhs.text}")
                                sys.exit(1)

                        elif current_token.type == "STAR":
                            lhs = self.lexer.tokens[self.lexer.token_pos - 1]

                            arguments.pop()

                            rhs = self.lexer.next()

                            if lhs.type == "INTEGER":
                                if rhs.type == "INTEGER":
                                    binop = BinOp(
                                        Expr(int(lhs.text)), Expr(
                                            int(rhs.text)), "*"
                                    )

                                    arguments.append(binop)
                                elif rhs.type in ("DOUBLEQUOTEDSTRING", "SINGLEQUOTEDSTRING"):
                                    binop = BinOp(
                                        Expr(int(lhs.text)), Expr(
                                            str(rhs.text).replace('"', "").replace("'", "")), "*"
                                    )

                                    arguments.append(binop)
                            elif lhs.type in ("DOUBLEQUOTEDSTRING", "SINGLEQUOTEDSTRING"):
                                if rhs.type == "INTEGER":
                                    binop = BinOp(
                                        Expr(str(lhs.text.replace('"', "").replace("'", ""))), Expr(
                                            int(rhs.text)), "*"
                                    )

                                    arguments.append(binop)
                                elif rhs.type in ("DOUBLEQUOTEDSTRING", "SINGLEQUOTEDSTRING"):
                                    sys.stderr.write(
                                        f"Cannot multuply STRING {lhs.text} by STRING {rhs.text}")
                                    sys.exit(1)
                        elif current_token.type == "SLASH":
                            lhs = self.lexer.tokens[self.lexer.token_pos - 1]

                            arguments.pop()

                            rhs = self.lexer.next()

                            if lhs.type == "INTEGER":
                                if rhs.type == "INTEGER":
                                    binop = BinOp(
                                        Expr(int(lhs.text)), Expr(
                                            int(rhs.text)), "/"
                                    )

                                    arguments.append(binop)
                                elif rhs.type in ("DOUBLEQUOTEDSTRING", "SINGLEQUOTEDSTRING"):
                                    sys.stderr.write(
                                        f"Cannot divide STRING {rhs.text} by INTEGER {lhs.text}")
                                    sys.exit(1)
                            elif lhs.type == "STRING":
                                sys.stderr.write(
                                    f"Cannot divide using STRING {lhs.text}")
                                sys.exit(1)
                        elif current_token.type == "IDENT":
                            name = self.lexer.current_token.text

                            next_token = self.lexer.peek()

                            if next_token.type == "ASSIGNMENT":
                                sys.stderr.write(
                                    "Cannot assign variables inside CHATTER")
                                sys.exit(1)

                            else:
                                variable = VariableExpr(name)

                                arguments.append(variable)
                else:
                    for token in self.lexer.tokens:
                        print(token.type)
                    print(current_token.text)
                    sys.stderr.write(
                        f"Invalid Syntax; expected '(', found {self.lexer.peek().text}")
                    sys.exit(1)

                chatter = FunctionCall("chatter", arguments)

                ast.append(chatter)

            elif self.lexer.current_token.type == "IDENT":
                name = self.lexer.current_token.text

                next_token = self.lexer.peek()

                if next_token.type != "ASSIGNMENT":
                    variable = VariableExpr(name)

                    ast.append(variable)

                    continue

                equals = self.lexer.next()

                value = self.lexer.next()

                if value.type == "INTEGER":
                    value = Expr(int(value.text))
                elif value.type in ("DOUBLEQUOTEDSTRING", "SINGLEQUOTEDSTRING"):
                    value = Expr(str(value.text).replace(
                        '"', "").replace("'", ""))
                else:
                    sys.stderr.write(
                        f"Invalid value given; Expected STRING or INTEGER, found {value.type}: {value.text}"
                    )
                    sys.exit(1)

                assignment_expr = AssignmentExpr(name, value)

                ast.append(assignment_expr)

            elif self.lexer.current_token.type == "EOF":
                break

        return ast
