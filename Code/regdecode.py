# dictionary used to contain register numeric values
registers = {
    "R0": 0,
    "R1": 1,
    "R2": 2,
    "R3": 3,
    "R4": 4,
    "R5": 5,
    "R6": 6,
    "R7": 7,
}

def reg_decode(func_type, instr, regs):
    # execution for r-type functions
    if func_type == "r":

        # special case for MIPS shifts
        """if (instr == "SLL") or (instr == "SRL"):
            try:
                # return[rs,        rt,               rd,             shamt]
                return [0, registers[regs[0]], registers[regs[1]], int(regs[2])]
            except:
                return None
        # END IF"""
                # special case for MIPS jr
        if instr == "JR":
            try:
                # return[        rs,        rt, rd,shamt]
                return [registers[regs[0]], 0, 0, 0]
            except:
                return None
        # END IF

        if instr == "IN":
            try:
                return[0, 0, registers[regs[2]], 0]
            except:
                return None
        if  instr == "OUT":
            try:
                return[registers[regs[0]], 0, 0, 0]
            except:
                return None
                # standard r-type MIPS instructions
        try:
            # return[      rs,                 rt,               rd,          shamt]
            return [registers[regs[0]], registers[regs[1]], registers[regs[2]], 0]
        except:
            return None



    # execution for i-type functions
    elif func_type == "i":

        # special case for lw, sw
        if (instr == "LW") or (instr == "SW"):
            try:

                #testing condition, is i/p hexa or not
                #[2][1] = 2nd col in reg[2] data = 0xblablabla, >1 y3nii worthy y7wlo wla l2

                if len(regs[2]) > 1 and regs[2][1] == "x":
                    #base hexa
                    imm = int(regs[2], base=16)
                else:
                    imm = int(regs[2])
                #               regs[0]                regs[1]         Regs[2]
                # return[       rs,                rt        ,  immediate  ]
                return [registers[regs[0]], registers[regs[1]], imm]
            except:
                return None
        if instr == "MOVI":
            try:
                if len(regs[1]) > 1 and regs[1][1] == "x":
                    imm = int(regs[1], base=16)
                else:
                    imm = int(regs[1])
                    #R0 R1
                #return [rd, imm]
                return [registers[regs[0]],imm]
            except:
                return None

        # standard i-type MIPS instructions
        try:
            if len(regs[2]) > 1 and regs[2][1] == "x":
                imm = int(regs[2], base=16)
            else:
                imm = int(regs[2])

            # return[        rs                 rt             immediate ]
            return [registers[regs[0]], registers[regs[1]], imm]
        except:
            return None

    # execution for j-type functions
    elif func_type == "j":
        try:
            if len(regs[0]) > 1 and regs[0][1] == "x":
                imm = int(regs[0], base=16)
            else:
                imm = int(regs[0])

                # return [ immediate ]
            return [imm]
        except:
            return None

    else:
        return None