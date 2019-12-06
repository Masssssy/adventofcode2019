import math

f = open("input", "r")

total_requirement = 0

for row in f:
  toAdd = math.floor(int(row)/3)-2
  total_requirement += toAdd

  extraFuel = toAdd
  while((math.floor(int(extraFuel)/3)-2) > 0):
      extraFuel = math.floor(int(extraFuel)/3)-2
      total_requirement += extraFuel;

print(total_requirement)
