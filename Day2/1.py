import math

f = open("input", "r")
array = f.read().split(",")
array = [ int(x) for x in array ]

array[1] = 12
array[2] = 2

print(array)

done = False
pointer = 0;
while(not done):
    if(array[pointer] == 99):
        break

    r1 = array[pointer+1]
    r2 = array[pointer+2]
    storeAt = array[pointer+3]

    if(array[pointer] == 1):
        array[storeAt] = array[r1]+array[r2]
        print(array[storeAt])

    elif(array[pointer] == 2):
        array[storeAt] = array[r1]*array[r2]

    pointer += 4

print(array[0])
