import math

f = open("input", "r")
array = f.read().split("\n")
#array = [ int(x) for x in array ]


path1 = []
path2 = []

#print(grid)

wire1 = array[0].split(",")
wire2 = array[1].split(",")

wire1Pos = [0,0];
steps = 0
for step in wire1:
    distance = int(step[1:])

    if step.startswith("U"):
        for x in range(distance):
            steps += 1
            wire1Pos[1] += 1;
            path1.append([[wire1Pos[0],wire1Pos[1]], steps])
            #grid[wire1Pos[0]][wire1Pos[1]]= True
    if step.startswith("D"):
        for x in range(distance):
            steps += 1
            wire1Pos[1] -= 1;
            path1.append([[wire1Pos[0],wire1Pos[1]], steps])
    if step.startswith("R"):
        for x in range(distance):
            steps += 1
            wire1Pos[0] += 1;
            path1.append([[wire1Pos[0],wire1Pos[1]], steps])
    if step.startswith("L"):
        for x in range(distance):
            steps += 1
            wire1Pos[0] -= 1;
            path1.append([[wire1Pos[0],wire1Pos[1]], steps])

wire2Pos = [0,0];
steps = 0
for step in wire2:
    distance = int(step[1:])

    if step.startswith("U"):
        for x in range(distance):
            steps += 1
            wire2Pos[1] += 1;
            path2.append([[wire2Pos[0],wire2Pos[1]], steps])
            #grid[wire2Pos[0]][wire2Pos[1]]= True
    if step.startswith("D"):
        for x in range(distance):
            steps += 1
            wire2Pos[1] -= 1;
            path2.append([[wire2Pos[0],wire2Pos[1]], steps])
    if step.startswith("R"):
        for x in range(distance):
            steps += 1
            wire2Pos[0] += 1;
            path2.append([[wire2Pos[0],wire2Pos[1]], steps])
    if step.startswith("L"):
        for x in range(distance):
            steps += 1
            wire2Pos[0] -= 1;
            path2.append([[wire2Pos[0],wire2Pos[1]], steps])


path1tuple = [tuple(l[0]) for l in path1]
path2tuple = [tuple(l[0]) for l in path2]
common = list(set(path1tuple).intersection(path2tuple))

nearest = 999999999
for point in common:
    distance = abs(0-point[0]) + abs(0-point[1])
    if(distance < nearest):
        nearest = distance

print("Nearest " + str(nearest))

smallest = 99999999999
for intersection in common:
    coord = [intersection[0],intersection[1]]

    stepsP1 = [i[1] for i in path1 if i[0] == coord][0]
    stepsP2 = [i[1] for i in path2 if i[0] == coord][0]
    sum = stepsP1 + stepsP2

    if(sum < smallest):
        smallest = sum

print("Smallest " + str(smallest))
