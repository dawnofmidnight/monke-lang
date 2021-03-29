class FunctionCall:
    def __init__(self, name, arguments):
        self.name = name
        self.arguments = arguments


class Expr:
    def __init__(self, value):
        self.value = value