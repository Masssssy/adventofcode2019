import math

f = open("input", "r")
array = f.read().split(",")
array = [int(x) for x in array ]


done = False
pointer = 0;
while(not done):

    print("pointer at instr "  + str(array[pointer]))
    opcode = str(array[pointer])[-2:]
    #print("op code " + str(opcode))
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

    #print("a " + str(a) + "  b " + str(b) + " c " + str(c))

    if(opcode == "99"):
        break

    if(opcode == "01" or opcode == "1"):
        #print("op1")
        if(c == 1):
            r1 = array[pointer+1]
        else:
            r1 = array[array[pointer+1]]

        if(b == 1):
            r2 = array[pointer+2]
        else:
            r2 = array[array[pointer+2]]

        r3 = array[pointer+3]
        array[r3] = r1 + r2
        pointer += 4

    elif(opcode == "02" or opcode == "2"):
        #print("op2")
        if(c == 1):
            r1 = array[pointer+1]
        else:
            r1 = array[array[pointer+1]]

        if(b == 1):
            r2 = array[pointer+2]
        else:
            r2 = array[array[pointer+2]]

        r3 = array[pointer+3]
        array[r3] = r1 * r2
        pointer += 4

    elif(opcode == "03" or opcode == "3"):
        #print("op 3")
        storeAt = array[pointer+1]
        #print(storeAt)
        array[storeAt] = 5
        pointer += 2

    elif(opcode == "04"  or opcode == "4"):
        if(c == 1):
            r1 = array[pointer+1]
        else:
            r1 = array[array[pointer+1]]

        print("OUTPUT " + str(r1))
        pointer += 2

    elif(opcode == "05"  or opcode == "5"):
        if(c == 1):
            r1 = array[pointer+1]
        else:
            r1 = array[array[pointer+1]]

        if(b == 1):
            r2 = array[pointer+2]
        else:
            r2 = array[array[pointer+2]]

        if(r1 != 0):
            pointer = r2
        else:
            pointer += 3


    elif(opcode == "06"  or opcode == "6"):
        if(c == 1):
            r1 = array[pointer+1]
        else:
            r1 = array[array[pointer+1]]

        if(b == 1):
            r2 = array[pointer+2]
        else:
            r2 = array[array[pointer+2]]

        if(r1 == 0):
            pointer = r2
        else:
            pointer += 3

    elif(opcode == "07"  or opcode == "7"):
                if(c == 1):
                    r1 = array[pointer+1]
                else:
                    r1 = array[array[pointer+1]]

                if(b == 1):
                    r2 = array[pointer+2]
                else:
                    r2 = array[array[pointer+2]]


                r3 = array[pointer+3]
                if(r1 < r2):
                    array[r3] = 1
                else:
                    array[r3] = 0
                pointer += 4


    elif(opcode == "08"  or opcode == "8"):
                if(c == 1):
                    r1 = array[pointer+1]
                else:
                    r1 = array[array[pointer+1]]

                if(b == 1):
                    r2 = array[pointer+2]
                else:
                    r2 = array[array[pointer+2]]


                r3 = array[pointer+3]
                if(r1 == r2):
                    array[r3] = 1
                else:
                    array[r3] = 0
                pointer += 4
