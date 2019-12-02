import csv

with open('input.txt', 'r') as inputFile:
    originalData = list(map(int, sum(list(csv.reader(inputFile)), [])))


for a in range (100):
    for b in range (100):
        data = originalData[:]
        data[1] = a
        data[2] = b
        x = 0
        while True:
            (i,p1,p2,p3) = data[x : x + 4]
            if i == 1:
                data[p3] = data[p1] + data[p2]
            elif i == 2:
                data[p3] = data[p1] * data[p2]
            else:
                assert i == 99
                if data[0] == 19690720:
                    print((a*100) + b)
                break
            x += 4
        
