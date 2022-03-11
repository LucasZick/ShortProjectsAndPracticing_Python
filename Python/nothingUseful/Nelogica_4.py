import sys

try:
    bigHits = 3
    newtons = [1, 4, 9, 2, 3]


    pointerList = newtons
    newtons = []
    for i in pointerList:
        newtons.append([i, pointerList.index(i)])
    pointerList.sort()


    bigHammer = []
    if bigHits > 0:
        bigHammer = pointerList[-bigHits:]

    bigCount = 0
    smallCount = 0

    bigBricks = [-1]
    smallBricks = [-1]

    for i in pointerList:
        if i in bigHammer:
            if bigBricks[0] == -1:
                bigBricks = []
            for j in newtons:
                if i == j[0]:
                    bigBricks.append(j[1]+1)
            bigHammer.pop(bigHammer.index(i))
            bigCount += 1

        else:
            if smallBricks[0] == -1:
                smallBricks = []
            for k in newtons:
                if i == k[0]:
                    smallBricks.append(k[1]+1)
            smallCount = smallCount + i

    total = bigCount + smallCount
    bigBricks.sort()
    smallBricks.sort()

    sys.stdout.write(str(total))
    sys.stdout.write('\n')

    for i in bigBricks:
        sys.stdout.write(str(i)+' ')
    sys.stdout.write('\n')


    for i in smallBricks:
        sys.stdout.write(str(i)+' ')
    sys.stdout.write('\n')
except ValueError as error:
    sys.stdout.write(error)