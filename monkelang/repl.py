import compiler
import monke_parser
import vm


def repl():
    """
    This function defines the debugging monkelang REPL environment. It runs 
    code with the VM class's run_once method.
    """
    machine = vm.VM([])
    monke_compiler = compiler.Compiler([])

    print("MonkeLang REPL (BETA)")

    while True:
        command = input("monke> ")

        ast = monke_parser.MonkeParser(command).parse()
                
        monke_compiler.ast = ast

        code, constant_table = monke_compiler.compile()
                

        machine.constant_table = constant_table
        machine.code = code

        machine.run_once(code)


repl()
