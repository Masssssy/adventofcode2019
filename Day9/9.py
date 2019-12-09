import math
import itertools

f = open("input", "r")
mem = f.read().split(",")
mem = [int(x) for x in mem]

for b in range(100000):
        mem.append(0)

array = mem
done = False
pointer = 0
input = 2
relativeBase = 0

while(not done):
    #print("pointer at instr "  + str(array[pointer]))
    opcode = str(array[pointer])[-2:]
    print("op code " + str(opcode))
    try:
        c = str(array[pointer])[-3]
        c = int(c)
        if(c == "-"):
            c = 0
    except:
        c = 0
    try:
        b = str(array[pointer])[-4]
        b = int(b)
        if(b == "-"):
            b = 0
    except:
        b = 0
    try:
        a = str(array[pointer])[-5]
        a = int(a)
        if(a == "-"):
            a = 0
    except:
        a = 0

    try:
        if(c == 1):
            r1 = array[pointer+1]
        elif(c == 0):
            r1 = array[array[pointer+1]]
        elif(c == 2):
            r1 = array[relativeBase + array[pointer+1]]
    except:
            print("could not set r1")

    try:
        if(b == 1):
            r2 = array[pointer+2]
        elif(b == 0):
            r2 = array[array[pointer+2]]
        elif(b == 2):
            r2 = array[relativeBase + array[pointer+2]]
    except:
        print("could not set r2")

    try:
        if(a == 1):
            r3 = array[pointer+3]
        elif(a == 0):
            r3 = array[array[pointer+3]]
        elif(a == 2):
            r3 = array[relativeBase + array[pointer+3]]
    except:
        print("could not set r3")

    if(opcode == "99"):
        break

    if(opcode == "01" or opcode == "1"):
        if(a == 2):
            r3 = relativeBase + array[pointer+3]
        else:
            r3 = array[pointer+3]
        array[r3] = r1 + r2
        pointer += 4

    elif(opcode == "02" or opcode == "2"):
        if(a == 2):
            r3 = relativeBase + array[pointer+3]
        else:
            r3 = array[pointer+3]
        array[r3] = r1 * r2
        pointer += 4

    elif(opcode == "03" or opcode == "3"):
        if(c == 2):
            r1 = relativeBase + array[pointer+1]
        else:
            r1 = array[pointer+1]

        array[r1] = input
        pointer += 2

    elif(opcode == "04"  or opcode == "4"):
        print("OUTPUT " + str(r1))
        pointer += 2

    elif(opcode == "05"  or opcode == "5"):
        if(r1 != 0):
            pointer = r2
        else:
            pointer += 3


    elif(opcode == "06"  or opcode == "6"):
        if(r1 == 0):
            pointer = r2
        else:
            pointer += 3

    elif(opcode == "07"  or opcode == "7"):
        if(a == 2):
            r3 = relativeBase + array[pointer+3]
        else:
            r3 = array[pointer+3]

        if(r1 < r2):
            array[r3] = 1
        else:
            array[r3] = 0
        pointer += 4


    elif(opcode == "08"  or opcode == "8"):
        if(a == 2):
            r3 = relativeBase + array[pointer+3]
        else:
            r3 = array[pointer+3]
        if(r1 == r2):
            array[r3] = 1
        else:
            array[r3] = 0
        pointer += 4

    elif(opcode == "09"  or opcode == "9"):
        relativeBase += r1
        pointer += 2