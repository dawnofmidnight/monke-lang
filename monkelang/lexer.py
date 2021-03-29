"""
MonkeLangs custom lexer
"""

import re
import sys

TOKEN_EXPRS = [
    (r"[\+|-]?[0-9]+", "INTEGER"),
    (r"\(", "LBRACE"),
    (r"\)", "RBRACE"),
    (r"[ \n\t]+", None),
    (r"chatter", "CHATTER"),
    (r"\"(?s:[^\"\\\\]|\\\\.)*\"", "DOUBLEQUOTEDSTRING"),
    (r"'(?s:[^'\\\\]|\\\\.)*'", "SINGLEQUOTEDSTRING"),
]


class Lexer:
    def __init__(self, string_input, token_exprs=TOKEN_EXPRS):
        self.source = string_input
        self.current_token = ""
        self.current_pos = 0
        self.token_pos = -1
        self.tokens = []
        self.token_exprs = token_exprs

    def lex(self):
        while self.current_pos < len(self.source):
            match = None
            for token_expr in self.token_exprs:
                pattern, tag = token_expr
                regex = re.compile(pattern)

                match = regex.match(self.source, self.current_pos)

                if match:
                    text = match.group(0)
                    if tag:
                        token = Token(text, tag)
                        self.tokens.append(token)
                    break

            if not match:
                sys.stderr.write(
                    f"Invalid Syntax: {self.source[self.current_pos]}")
                sys.exit(1)
            else:
                self.current_pos = match.end(0)

    def next(self):
        self.token_pos += 1

        if self.token_pos >= len(self.tokens):
            self.current_token = Token("EOF", "EOF")
        else:
            self.current_token = self.tokens[self.token_pos]

        return self.current_token

    def peek(self):
        if self.token_pos + 1 >= len(self.tokens):
            return Token("EOF", "EOF")
        else:
            return self.tokens[self.token_pos + 1]


class Token:
    def __init__(self, text, type):
        self.text = text
        self.type = type
