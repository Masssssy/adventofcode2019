import math

f = open("input", "r")

total_requirement = 0

for row in f:
  total_requirement += math.floor(int(row)/3)-2

print(total_requirement)
