import math

f = open("input", "r")
orbits = f.read().split("\n")

orbitDict = dict()

for orbit in orbits:
    around = orbit.split(")")[0]
    orbiting = orbit.split(")")[1]

    if(not orbiting in orbitDict):
        orbitDict[orbiting] = [around]
    else:
        orbitDict[orbiting].append(around)

directCount = 0
indirectCount = 0

youPath = []
sanPath = []

for planet in orbitDict:
    directOrbits = orbitDict[planet]
    directCount += len(directOrbits)

    toProcess = directOrbits.copy()
    while(len(toProcess) > 0):
        child = toProcess.pop()
        if child in orbitDict:
            childrenToChild = orbitDict[child]
            indirectCount += len(childrenToChild)
            if(planet == "YOU"):
                youPath.append(childrenToChild)
            if(planet == "SAN"):
                sanPath.append(childrenToChild)
            for child in childrenToChild:
                toProcess.append(child)

print(directCount + indirectCount)

print(youPath)
print(sanPath)

commonOrbits = [i for i in youPath if i in sanPath]

lowest = 99999999
for common in commonOrbits:
    youDist = youPath.index(common) + 1
    sanDist = sanPath.index(common) + 1
    dist = youDist + sanDist
    if(dist < lowest):
        lowest = dist

print(lowest)






