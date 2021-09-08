def instr_decode(instr):
    if instr == "ADD":
        func_type = "r"
        opcode = 0x0
        funct = 0x0

    elif instr == "SUB":
        func_type = "r"
        opcode = 0x0
        funct = 0x1

    elif instr == "AND":
        func_type = "r"
        opcode = 0x0
        funct = 0x2

    elif instr == "OR":
        func_type = "r"
        opcode = 0x0
        funct = 0x3

    elif instr == "NOR":
        func_type = "r"
        opcode = 0x0
        funct = 0x4

    elif instr == "XOR":
        func_type = "r"
        opcode = 0x0
        funct = 0x5

    elif instr == "SLL":
        func_type = "r"
        opcode = 0x0
        funct = 0x6

    elif instr == "SRL":
        func_type = "r"
        opcode = 0x0
        funct = 0x7

    elif instr == "IN":
        func_type = "r"
        opcode = 0x1
        funct = 0x0

    elif instr == "OUT":
        func_type = "r"
        opcode = 0x2
        funct = 0x0

    elif instr == "JR":
        func_type = "r"
        opcode = 0x3
        funct = 0x0

    elif instr == "ADDI":
        func_type = "i"
        opcode = 0x4
        funct = None

    elif instr == "ANDI":
        func_type = "i"
        opcode = 0x5
        funct = None

    elif instr == "ORI":
        func_type = "i"
        opcode = 0x6
        funct = None

    elif instr == "LW":
        func_type = "i"
        opcode = 0x7
        funct = None

    elif instr == "SW":
        func_type = "i"
        opcode = 0x8
        funct = None

    elif instr == "BEQ":
        func_type = "i"
        opcode = 0x9
        funct = None

    elif instr == "BNE":
        func_type = "i"
        opcode = 0xa
        funct = None

    elif instr == "MOVI":
        func_type = "i"
        opcode = 0xd
        funct = None

    elif instr == "J":
        func_type = "j"
        opcode = 0xb
        funct = None

    elif instr == "JAL":
        func_type = "j"
        opcode = 0xc
        funct = None

    elif instr == "NOP":
        func_type = None
        opcode = 0xe
        funct = None

    elif instr == "HLT":
        func_type = None
        opcode = 0xf
        funct = None

    else:
        func_type = None
        opcode = None
        funct = None

    # returns an array
    return [func_type, opcode, funct]