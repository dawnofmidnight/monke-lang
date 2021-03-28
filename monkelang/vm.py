from inspect import signature
import sys


class VM:
    def __init__(self, code):
        self.code = code
        self.stack = []
        self.pc = 0
        self.constant_table = []

    def LOAD_VALUE(self, argument):
        value = self.constant_table[argument]
        self.stack.append(value)
        self.pc += 1

    def PRINT_VALUE(self):
        value = self.stack.pop()

        print(value)

        self.pc += 1

    def run(self):
        while True:
            if self.pc >= len(self.code):
                sys.exit()

            instruction = self.code[self.pc]

            function = getattr(self, instruction[0])

            sig = signature(function)

            if len(sig.parameters) == 2:
                function(instruction[1])
            else:
                function()

    def run_once(self, code):
        while True:
            if self.pc >= len(code):
                sys.exit()

            instruction = code[self.pc]

            function = getattr(self, instruction[0])

            sig = signature(function)

            if len(sig.parameters) == 1:
                function(instruction[1])
            else:
                function()
