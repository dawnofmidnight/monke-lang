class FunctionCall:
    """
    This AST is used to represent function calls, and takes
    a name (string) for the function call and a list of arguments
    that need to be provided to the function.
    """

    def __init__(self, name, arguments):
        self.name = name
        self.arguments = arguments


class Expr:
    """
    This class is used to represent all expressions
    Expressions compose of strings, integers, and floats.
    The class takes a single value argument.
    """

    def __init__(self, value):
        self.value = value


class BinOp:
    """
    This class is used to represent all binary operations.
    Binary operations include addition, subtraction, multiplication,
    and division. The class takes three arguments. lhs (left hand side),
    rhs (right hand side), and op (operator).
    """

    def __init__(self, lhs, rhs, op):
        self.lhs = lhs
        self.rhs = rhs
        self.op = op
