#import matplotlib.pyplot as plt
import sys
from sys import stdin 

def dec_to_bi(n):
    p = ''
    st = ''
    while n != 0:
        r = int(n)%2
        st = st+str(r)
        n = int(n)//2
        p = st[::-1]
    return(p)

def dec_to_bi_8(n):
    p =  ''
    st =  ''
    final_8 = ''
    while n != 0:
        r = int(n)%2
        st = st + str(r)
        n = int(n)//2
        p = st[::-1]
    len_ans = len(p)
    final_8 = '0'*(8-len_ans) + p
    return(final_8)

def dec_to_bi_16(n):
    p = ''
    st = ''
    final_16 = ''
    while n != 0:
        r = int(n)%2
        st = st+str(r)
        n = int(n)//2
        p = st[::-1]
    len_ans = len(p)
    final_16 = '0'*(16-len_ans) + p
    return(final_16)

def bi_to_dec(n):
    i = 0
    deci = 0
    while n != 0:
        p = int(n) % 10
        deci = deci + p*2**i
        i = i + 1
        n = int(n)//10
    return deci

input_sim = []
file = sys.stdin
for line in file:
    if '\n' == line:
        break
    list_instr = []
    for i in line.split():
        input_sim.append(i)

# '1001000100000101', '1001000100000101', '1001000100000101', '1001000100000101', '1001000100000101', '1001000100000101', '0101000000000000'
# '1001000100000101','1010100100000011', '0101000000000000']
# '1001000100000101', '1001000100000101', '1001000100000101', '1001000100000101', '1001000100000101', '1001000100000101', '0101000000000000'
# '1001100000001010', '1001100000001010', '1001100000001010', '1001100000001010', '1001100000001010', '1001100000001010', '0101000000000000'
# '1000100000001010', '1000100000001010', '1000100000001010', '1000100000001010', '1000100000001010', '1000100000001010', '1000100000001010','1000100000001010', '1000100000001010', '1000100000001010', '0101000000000000'
len_sim = len(input_sim)
pc_count = 0
prog_count = '00000000'
final_sim = []
cycle = 0
pc_list = []
cycle_list = []

mem_dump = []

mem_dump = input_sim.copy()
for l in range(256-len_sim):
    mem_dump.append('0000000000000000')

#to store value in 16- bit register
r0 = '0000000000000000'
r1 = '0000000000000000'
r2 = '0000000000000000'
r3 = '0000000000000000'
r4 = '0000000000000000'
r5 = '0000000000000000'
r6 = '0000000000000000'
flags = '0000000000000000'

A_sim = {'10000' : 'add', '10001' : 'sub', '10110': 'mul', '11010': 'xor', '11011': 'or', '11100': 'and'}

B_sim = {'10010' : 'mov', '11000': 'rs', '11001': 'ls'}

C_sim = {'10011': 'mov', '10111': 'div', '11101': 'not', '11110': 'cmp'}

D_sim = {'10100': 'ld', '10101': 'st'}

E_sim = {'11111': 'jmp', '01100': 'jlt', '01101': 'jgt', '01111': 'je'}

F_sim = {'01010': 'hlt'}

reg_value = {'000': r0,'001': r1,'010': r2,'011': r3,'100': r4,'101': r5,'110': r6, '111':flags}

i = 0
while i < len_sim:
    op_sim = input_sim[i][:5]

    #Type A
    if(op_sim in A_sim):
        a1 = input_sim[i][7:10]
        a2 = input_sim[i][10:13]
        a3 = input_sim[i][13:16]

        if(A_sim[op_sim] == 'add'):
            value1 = bi_to_dec(int(reg_value[a1]))
            value2 = bi_to_dec(int(reg_value[a2]))
            sum = value1 + value2
            if (value1+value2>255):
                reg_value[a3] = '1111111111111111'
            else:
                reg_value[a3] = dec_to_bi_16(sum)
            reg_value['111'] = '0000000000000000'

        elif(A_sim[op_sim] == 'sub'):
            value1 = bi_to_dec(int(reg_value[a1]))
            value2 = bi_to_dec(int(reg_value[a2]))
            diff = value1-value2
            if (value1-value2<0):
                reg_value[a3] ='0000000000000000'
            else:
                reg_value[a3] = dec_to_bi_16(diff)
            reg_value['111'] = '0000000000000000'

        elif(A_sim[op_sim] == 'mul'):
            value1 = bi_to_dec(int(reg_value[a1]))
            value2 = bi_to_dec(int(reg_value[a2]))
            prod=value1*value2
            if (value1*value2>255):
                reg_value[a3] = '1111111111111111'
            else:
                reg_value[a3] = dec_to_bi_16(prod)
            reg_value['111'] = '0000000000000000'

        elif(A_sim[op_sim] == 'xor'):
            for m in range(16):
                if reg_value[a1][m] == reg_value[a2][m]:
                    reg_value[a3][m] == 0
                else:
                    reg_value[a3][m] == 1
            reg_value['111'] = '0000000000000000'

        elif(A_sim[op_sim] == 'or'):
            for m in range(16):
                if reg_value[a1][m] == 0 and reg_value[a2][m] == 0:
                    reg_value[a3][m] == 0
                else:
                    reg_value[a3][m] == 1
            reg_value['111'] = '0000000000000000'

        elif(A_sim[op_sim] == 'and'):
            for m in range(16):
                if reg_value[a1][m] == 1 and reg_value[a2][m] == 1:
                    reg_value[a3][m] == 1
                else:
                    reg_value[a3][m] == 0
            reg_value['111'] = '0000000000000000'

    #Type B
    elif(op_sim in B_sim):
        b1 = input_sim[i][5:8]
        if(B_sim[op_sim] == 'mov'):
            reg_value[b1] = '00000000' + input_sim[i][8:]
            reg_value['111'] = '0000000000000000'

        elif(B_sim[op_sim] == 'rs'):
            value1 = bi_to_dec(int(reg_value[b1])) 
            value2= bi_to_dec(int(input_sim[i][8:]))
            ans=value1//(2**value2)   
            reg_value[b1] = dec_to_bi_16(ans)
            reg_value['111'] = '0000000000000000'

        elif(B_sim[op_sim] == 'ls'):
            value1 = bi_to_dec(int(reg_value[b1])) 
            value2= bi_to_dec(int(input_sim[i][8:]))
            ans=value1*(2**value2)   
            reg_value[b1] = dec_to_bi_16(ans)
            reg_value['111'] = '0000000000000000'
           
    #Type C
    elif(op_sim in C_sim):
        c1=input_sim[i][10:13]
        c2=input_sim[i][13:16]

        if(C_sim[op_sim] == 'mov'):
            reg_value[c2] = reg_value[c1]
            reg_value['111'] = '0000000000000000'

        elif(C_sim[op_sim]=='div'):
            value1 = bi_to_dec(int(reg_value[c1]))
            value2 = bi_to_dec(int(reg_value[c2]))
            quotient = value1/value2
            rem = value1%value2
            r0 = str(dec_to_bi(quotient))
            r1 = str(dec_to_bi(rem))
            reg_value['111'] = '0000000000000000'

        elif(C_sim[op_sim]=='not'):
            for m in range(16):
                    if reg_value[c1][m] == 1:
                        reg_value[c2][m] == 0
                    else:
                        reg_value[c2][m] == 1
            reg_value['111'] = '0000000000000000'
           
        elif(C_sim[op_sim]=='cmp'):
            value1 = bi_to_dec(int(reg_value[c1]))
            value2 = bi_to_dec(int(reg_value[c2]))
            if(value1<value2):
                reg_value['111'] = '0000000000000100'
            elif(value1>value2):
                reg_value['111'] = '0000000000000010'
            elif(value1==value2):
                reg_value['111'] = '0000000000000001'

    #Type D
    elif(op_sim in D_sim):
        mem_add = input_sim[i][8:16]
        x = bi_to_dec(int(mem_add))
        d1 = input_sim[i][5:8]
        if(D_sim[op_sim] == 'ld'):    #loads data of reg in mem dump
            reg_value[d1] = mem_dump[x]
            reg_value['111'] = '0000000000000000'

        elif(D_sim[op_sim] == 'st'):  #loads data of mem dump in reg
            mem_dump[x] = reg_value[d1]
            reg_value['111'] = '0000000000000000'

    #Type E
    elif(op_sim in E_sim):                          ###doubt
        mem_add = input_sim[i][8:16]
        x = bi_to_dec(int(mem_add))
        if(E_sim[op_sim]=='jmp'):
            mem = bi_to_dec(mem_add)
            i = mem - 1
            #jump to memory address
        elif(E_sim[op_sim]=='jlt' and flags[13]==1):
            mem = bi_to_dec(mem_add)
            i = mem - 1
            #jump to memory address
        elif(E_sim[op_sim]=='jgt' and flags[14]==1):
            mem = bi_to_dec(mem_add)
            i = mem - 1
            #jump to memory address 
        elif(E_sim[op_sim]=='je' and flags[15]==1):
            mem = bi_to_dec(mem_add)
            i = mem - 1
            #jump to memory address
        reg_value['111'] = '0000000000000000'

    elif(op_sim in F_sim):
        if(F_sim[op_sim]=='hlt'):
            reg_value['111'] = '0000000000000000'
            res = dec_to_bi_8(i) + ' ' + reg_value['000'] + ' ' + reg_value['001'] + ' ' + reg_value['010'] + ' ' + reg_value['011'] + ' ' + reg_value['100'] + ' ' + reg_value['101'] + ' ' + reg_value['110'] + ' ' + reg_value['111']
            final_sim.append(res)
            pc_list.append(pc_count)
            cycle_list.append(cycle)
            break

    res = dec_to_bi_8(pc_count) + ' ' + reg_value['000'] + ' ' + reg_value['001'] + ' ' + reg_value['010'] + ' ' + reg_value['011'] + ' ' + reg_value['100'] + ' ' + reg_value['101'] + ' ' + reg_value['110'] + ' ' + reg_value['111']
    final_sim.append(res)
    # pc_count += 1
    i+=1
    pc_list.append(pc_count)
    cycle_list.append(cycle)
    pc_count = i
    cycle += 1

for r in range(len(final_sim)):
    print(final_sim[r])

for r in mem_dump:
    print(r)
# print(*mem_dump)
# plt.scatter(cycle_list, pc_list, label = "line 1")
# plt.title('Cycle-Pc')

#cmp R3 R4   (R3>R4)---14 = 1
#add R4 R5 R6 (R4>R3)
#jgt mem_address