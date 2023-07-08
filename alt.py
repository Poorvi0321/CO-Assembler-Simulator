import math
memorySpaceBytes={'B':0,'KB':10,'MB':20,'GB':30,'TB':40}

memorySpaceBits={'b':0,'Kb':7,'Mb':17,'Gb':27,'Tb':37}

def exitCode():
    quit()

print("Enter space in memory:")
mem_space=list(map(str,input().split()))
if(mem_space[1] not in memorySpaceBytes and memorySpaceBits):
    print("Format Invalid.")
    exitCode()
print('''Four types of memory are:
1.Bit Addressable Memory
2. Nibble Addressable Memory
3. Byte Addressable Memory 
4. Word Addressable Memory''')
mem_addressesd=int(input("How the memory is addressed as mentioned above? Either of the 4 options:"))


##TYPE 1(ISA related)
#a                                     ###doubt
inst_len=int(input("Length of instruction in bits:"))
reg_len=int(input("Length of register in bits:"))
mem=int(mem_space[0])
add_bits_og=(math.log2(mem)+memorySpaceBytes[mem_space[1]])+3
if(mem_space[1] in memorySpaceBytes):
    if (mem_addressesd==1):
        add_bits=add_bits_og
    elif(mem_addressesd==2):
        add_bits=add_bits_og-2
    elif(mem_addressesd==3):
        add_bits=add_bits_og-3
    elif(mem_addressesd==4):
        add_bits=add_bits_og-3
        print("Since we are not taking input for CPU thus we are considering Byte adressable as default,as mentioned.")
    else:
        add_bits=add_bits_og-3
        print("Error! Since its not mentioned hpw memory is addressed we take byte adressable as default.")
        exitCode()
elif(mem_space[1] in memorySpaceBits):
    if (mem_addressesd==1):
        add_bits=add_bits_og-3
    elif(mem_addressesd==2):
        add_bits=add_bits_og-5
    elif(mem_addressesd==3):
        add_bits=add_bits_og-6
    elif(mem_addressesd==4):
        add_bits=add_bits_og-6
        print("Since we are not taking input for CPU thus we are considering Byte adressable as default,as mentioned.")
    else:
        add_bits=add_bits_og-6
        print("Error! Since its not mentioned how memory is addressed we take Byte adressable as default.")
        exitCode()
    
if(add_bits<0):
    print("Error! Length of address is more than length of instruction.")
    exitCode()
else:
    print("Minimum number of bits to represent an address:",add_bits)

#b
op_len=inst_len-(reg_len+add_bits)
if(op_len<0):
    print("Error! Opcode length is invalid.")
    exitCode()
else:
    print("Number of bits needed by opcode:",op_len)
#c
filler_len=inst_len-(op_len+2*reg_len)
if(filler_len<0):
    print("Error! Length of filler bits invalid.")
    exitCode()

else:
    print("Number of filler bits in instruction Type B:",filler_len)
#d                  ##doubt
max_inst=2**op_len
print("Maximum number of instructions this ISA can support:",max_inst)
#e
max_reg=(2**reg_len)-1
print("Maximum number of registers supported by ISA:",max_reg)

#TYPE2
#TYPE 1(system enhanceent related)
cpu_bits=int(input("How many bits is the CPU?:"))
change=int(input("How would you want to change the current addressable memory to any of the rest 3 options?:"))
cpu_log=math.log2(cpu_bits)

if(change==1):
    new_add_bits=add_bits_og
elif(change==2):
    new_add_bits=add_bits_og-2
elif(change==3):
    new_add_bits=add_bits_og-3
elif(change==4):
    new_add_bits=add_bits_og-cpu_log
else:
    new_add_bits=add_bits_og-3

pin_diff=new_add_bits-add_bits
print(pin_diff)

#TYPE 2
cpu_bits2=int(input("How many bits is the CPU?:"))
add_pins=int(input("Number of address pins:"))
mem_addressable=int(input("What type of addressable memory it has?: "))

cpu_log2=math.log2(cpu_bits2)

if(mem_addressable==1):
    space2=(add_pins-3)    
elif(mem_addressable==2):
    space2=(add_pins-1)
elif(mem_addressable==3):
    space2=(add_pins)
elif(mem_addressable==4):
    space2=(add_pins+cpu_log2-3)
else:
    space2=(add_pins)


power=space2%10
val=2**(power)
val_final=str(val)

unit=space2-power
key_list = list(memorySpaceBytes.keys())
val_list = list(memorySpaceBytes.values())

position=val_list.index(unit)
unit_final=key_list[position]
print(val_final+unit_final)
exit()