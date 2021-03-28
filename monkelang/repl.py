import compiler
import monke_parser
import vm


def repl():
    machine = vm.VM([])
    monke_compiler = compiler.Compiler([])

    print("MonkeLang REPL (BETA)")

    while True:
        command = input("> ")

        ast = monke_parser.MonkeParser(command).parse()
        
        monke_compiler.ast = ast

        code, constant_table = monke_compiler.compile()
        

        machine.constant_table = constant_table
        machine.code = code

        machine.run_once(code)


repl()
