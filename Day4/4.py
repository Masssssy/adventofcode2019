import math

start = 240298
end = 784956

okPasswords = 0

i = start
while(i <= end):
    adjacent = False
    increasing = True

    string = str(i)

    lowest = int(string[0])
    for b in string:
        if(not (int(b) >= lowest)):
            #not ok
            increasing = False
            break
        else:
            lowest = int(b)


    #check adjacent
    streak = 0
    for b in range(len(string)-1):
        #print(streak)
        if(string[b] == string[b+1]):
            streak += 1
        else:
            #streak broken
            if(streak == 1):
                adjacent = True
            streak = 0
    if(streak == 1):
        adjacent = True

    if(adjacent and increasing):
        okPasswords += 1

    i += 1;

print(okPasswords)
