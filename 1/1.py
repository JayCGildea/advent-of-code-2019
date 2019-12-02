import math

with open('input.txt') as inputFile:
    inputs = list(inputFile)
    print(sum([math.floor(int(x)/3) - 2 for x in inputs]))