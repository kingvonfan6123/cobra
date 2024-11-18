import cobra

code = """
show->Hello World!
"""

bytecode, size = cobra.cobra_bytecode.compile(code)

cobra.run_bytecode(bytecode, size)
