"""
Written by @virtualqueryex [Ad] on 11-18-2024
Name: Cobra [Python]
Description: Interpretter (main) module [to run compiled bytecode]
"""

import cobra_bytecode
import cobra_utilities

# import globals from bytecode module #
OP_PRINT = cobra_bytecode.OP_PRINT
bytecode_map = cobra_bytecode.bytecode_map
char_map = cobra_bytecode.char_map

def run_bytecode(bytecode, size):
    if ((size == 0) or (len(bytecode) != size)):
        cobra_utilities.throw_error("Bytecode size mismatch, Failed to run bytecode.", -1)

    i = 0
    while i < len(bytecode):
        opcode = bytecode[i]
        i += 1
        if opcode == OP_PRINT:
            output = ""
            while i < len(bytecode) and bytecode[i] != bytecode_map['\n']:
                output += char_map[bytecode[i]]
                i += 1
            i += 1
            print(output)
        else:
            cobra_utilities.throw_error("Invalid bytecode! Failed to run bytecode.", -1)