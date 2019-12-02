import math

def include_extra_fuel(fuel):
    toAdd = math.floor(fuel/3)-2
    if (toAdd > 0):
        return fuel + include_extra_fuel(toAdd)
    return fuel

with open('input.txt') as inputFile:
    inputs = list(inputFile)
    print(sum([include_extra_fuel(math.floor(int(x)/3) - 2) for x in inputs]))