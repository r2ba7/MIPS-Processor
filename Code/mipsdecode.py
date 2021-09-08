# Converts MIPS instructions into binary and hex
import os
import sys
import time
from instrdecode import instr_decode
from regdecode import reg_decode

# the main conversion function
def convert(code):

    code = code.replace("(", " ")
    code = code.replace(")", "")
    code = code.replace("[", " ")
    code = code.replace("]", "")
    code = code.replace(",", " ")
    code = code.replace("  ", " ")
    args = code.split(" ")
    # instruction "string" by3rf3na l function 3obara 3n a zy halt aw add
    instruction = args[0]
    # instruction is string
    if instruction == "HLT":
        sys.exit()

    if instruction == "NOP":
        time.sleep(5)
        print("Delayed for 5.")

    # codes[0,1,2] -> [func_type, opcode, funct]
    codes = instr_decode(instruction)
    # codes  = array which is [func_type, opcode, funct]
    func_type = codes[0]
    # reg_decode(func_type, instr, regs)
    reg_values = reg_decode(func_type, instruction, args[1:])  # get the numeric values of the registers

    # the following if statement below prints an error if needed
    if reg_values == None:
        if instruction == "NOP":
            return
        print("Not a valid MIPS statement")

    # execution for r-type functions
    if func_type == "r":
        """if (instruction == "SLL") or (instruction == "SRL"):
            opcode = '{0:04b}'.format(codes[1])
            rt = '{0:03b}'.format(reg_values[1])
            rd = '{0:03b}'.format(reg_values[2])
            shamt = '{0:03b}'.format(int(reg_values[3]))
            funct = '{0:03b}'.format(codes[2])
            print("Function type: R-Type")
            print("Instruction form: opcode| rt |  rd | shamt | funct")
            print("Formatted binary: " + opcode + "|" + rt + "|" + rd + "|" + shamt + "|" + funct)
            binary = "0b" + opcode + rt + rd + shamt + funct
            print("Binary:           " + binary)
            hex_string = '{0:08x}'.format(int(binary, base=2))
            print("Hex:              0x" + hex_string)
            print("--------------------------------------------------------------------------------")
        # .format bt4iil l mbeen square braccets w t7ot l codes[1], aw bm3na tanii bt4iil awl parameter w t7ot l gwa l format
        # for Shift left and right, hn3ml nested if mn 7is hyb2a leeha l conditions w hy2ba leeha t2siimt register 5asa zy en e7na n4iil rt w n7ot shamt"""
        # codes  = array 3obara 3n [func_type, opcode, funct]
        opcode = '{0:04b}'.format(codes[1])
        rs = '{0:03b}'.format(reg_values[0])
        rt = '{0:03b}'.format(reg_values[1])
        rd = '{0:03b}'.format(reg_values[2])
        funct = '{0:03b}'.format(codes[2])
        print("Function type: R-Type")
        print("Instruction form: opcode|  rs |  rt |  rd | funct")
        print("Formatted binary: " + opcode + "|" + rs + "|" + rt + "|" + rd + "|" + funct)
        binary = "0b" + opcode + rs + rt + rd + funct
        print("Binary:           " + binary)
        hex_string = '{0:08x}'.format(int(binary, base=2))
        print("Hex:              0x" + hex_string)
        print("--------------------------------------------------------------------------------")

    # execution for i-type functions
    elif func_type == "i":
        # special case
        if instruction == "MOVI":

            opcode = '{0:04b}'.format(codes[1])
            rd = '{0:03b}'.format(reg_values[0])
            imm = '{0:09b}'.format(reg_values[1])
            print("Function type: I-Type")
            print("Instruction form: opcode| rd |   immediate      ")
            print("Formatted binary: " + opcode + "|" + rd + "|" + imm)
            binary = "0b" + opcode + rd  + imm
            print("Binary:           " + binary)
            hex_string = '{0:08x}'.format(int(binary, base=2))
            print("Hex:              0x" + hex_string)
            print("--------------------------------------------------------------------------------")

        else:
            opcode = '{0:04b}'.format(codes[1])
            rs = '{0:03b}'.format(reg_values[0])
            rt = '{0:03b}'.format(reg_values[1])
            imm = '{0:06b}'.format(reg_values[2])
            print("Function type: I-Type")
            print("Instruction form: opcode|  rs |  rt |   immediate      ")
            print("Formatted binary: " + opcode + "|" + rs + "|" + rt + "|" + imm)
            binary = "0b" + opcode + rs + rt + imm
            print("Binary:           " + binary)
            hex_string = '{0:08x}'.format(int(binary, base=2))
            print("Hex:              0x" + hex_string)
            print("--------------------------------------------------------------------------------")

    # execution for j-type functions
    elif func_type == "j":
        opcode = '{0:04b}'.format(codes[1])
        imm = '{0:012b}'.format(reg_values[0])
        print("Function type: J-Type")
        print("Instruction form: opcode| immediate")
        print("Formatted binary: " + opcode + "|" + imm)
        binary = "0b" + opcode + imm
        print("Binary:           " + binary)
        hex_string = '{0:08x}'.format(int(binary, base=2))
        print("Hex:              0x" + hex_string)
        print("--------------------------------------------------------------------------------")

    return


# main
print("Type MIPS code below to see it in binary and hex form")
print("Syntax: If using hex, use the '0x' label")
print("Type 'HLT' to halt")
print("--------------------------------------------------------------------------------")
while True:
    # team l assembly hwa l hydlna l MIPS code
    mips = input("Type MIPS code here: ")
    print()
    convert(mips)
