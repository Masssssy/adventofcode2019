import math
from colorama import init
from colorama import Fore, Back, Style
init() # init stupid ansi/ascii whatever for retarded windows

f = open("input", "r")
array = f.read()
array = [ int(x) for x in str(array)]

width = 25
height = 6

layers = []
layerSize = width * height
while(len(array) > 0):
    layers.append(array[:layerSize])
    array = array[layerSize:]

fewestZeros = 999999999
fewestIndex = None

i = 0
for layer in layers:
    zeros = layer.count(0)
    if(zeros < fewestZeros):
        fewestZeros = zeros
        fewestIndex = i

    i+=1
oneDigits = layers[fewestIndex].count(1)
twoDigits = layers[fewestIndex].count(2)
#Solution 1
print(oneDigits * twoDigits)

####### Part 2: Merge the layers ##############
layers.reverse() #start from the back
image = []
for pixel in range(layerSize):
    pixelColor = None
    for layer in layers:
        if(layer[pixel] != 2):
            pixelColor = layer[pixel]
    image.append(pixelColor)

rows = [image[i * 25:(i + 1) * 25] for i in range((len(image) + 25 - 1) // n )]
for row in rows:
    for c in row:
        if(c == 0):
            print(Fore.RED + str("█"), end= '')
        if(c == 1):
            print(Fore.GREEN + str("█"), end= '')
    print(" ")