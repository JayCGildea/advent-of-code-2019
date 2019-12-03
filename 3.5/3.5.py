import csv

def get_distance(x, y):
    return abs(x) + abs(y)

aCorner = []
bCorner = []

def calc_corners(x, y, moveList):
    if len(moveList) == 0:
        return []

    move = moveList[0]
    direction = move[0]
    distance = int(move[1:])

    if direction == 'U':
        y += distance
    elif direction == 'D':
        y -= distance
    elif direction == 'R':
        x += distance
    elif direction == 'L':
        x -= distance
    
    corners = calc_corners(x, y, moveList[1:])
    corners.append((x, y))
    return corners

with open('input.txt') as inputFile:
    data = list(csv.reader(inputFile))
    i1 = data[0]
    i2 = data[1]

    aCorner = calc_corners(0, 0, i1)
    bCorner = calc_corners(0, 0, i2)
    aCorner.reverse()
    bCorner.reverse()

    hits = []

    for i in range(len(aCorner)-1):
        for j in range(len(bCorner)-1):
            ax1 = aCorner[i][0]
            ax2 = aCorner[i+1][0]
            ay1 = aCorner[i][1]
            ay2 = aCorner[i+1][1]

            bx1 = bCorner[j][0]
            bx2 = bCorner[j+1][0]
            by1 = bCorner[j][1]
            by2 = bCorner[j+1][1]

            aHorizontal = ay1 == ay2
            bHorizontal = by1 == by2

            if aHorizontal and not bHorizontal:
                if (ax1 > bx1 > ax2 or ax1 < bx1 < ax2) and (by1 > ay1 > by2 or by1 < ay1 < by2):
                    hits.append((bx1, ay1))
            elif not aHorizontal and bHorizontal:
                if (bx1 > ax1 > bx2 or bx1 < ax1 < bx2) and (ay1 > by1 > ay2 or ay1 < by1 < ay2):
                    hits.append((ax1, by1))

    minDistance = None
    for hit in hits:
        dist = get_distance(hit[0], hit[1])
        if minDistance is None or minDistance > dist:
            minDistance = dist

    print(minDistance)


