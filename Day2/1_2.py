import math
import itertools

values = [(p1, p2) for p1 in range(100) for p2 in range(100) if p1 != p2]


done = False
i = 0
while not done:
    f = open("input", "r")
    array = f.read().split(",")
    array = [ int(x) for x in array ]

    array[1] = values[i][0]
    array[2] = values[i][1]

    pointer = 0;
    while(not done):
        if(array[pointer] == 99):
            break

        r1 = array[pointer+1]
        r2 = array[pointer+2]
        storeAt = array[pointer+3]

        if(array[pointer] == 1):
            array[storeAt] = array[r1]+array[r2]

        elif(array[pointer] == 2):
            array[storeAt] = array[r1]*array[r2]

        pointer += 4

    if(array[0] == 19690720):
        #print(array[0])
        print(str(values[i][0]))
        print(str(values[i][1]))
        print(100 * values[i][0] +values[i][1] )
    i+=1
