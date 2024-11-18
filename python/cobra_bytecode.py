"""
Written by @virtualqueryex [Ad] on 11-18-2024
Name: Cobra [Python]
Description: Bytecode module [to compile/decompile]
"""

OP_PRINT = 0x20
bytecode_map = {chr(i): i + 100 for i in range(32, 127)}
bytecode_map['\n'] = 0xFE
char_map = {v: k for k, v in bytecode_map.items()}

def compile(source_code):
    bytecode = []
    lines = source_code.splitlines()
    for line in lines:
        if line.startswith("show->"):
            text = line[6:].strip()
            bytecode.append(OP_PRINT)
            bytecode.extend(bytecode_map[char] for char in text)
            bytecode.append(bytecode_map['\n'])
    return (bytecode, len(bytecode))
