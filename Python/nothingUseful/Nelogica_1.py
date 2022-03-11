import sys


numbers = [2, 1, 3, 12, 4, 11, 5, 7, 19, 15]

try:
    minDiff = None
    results = []

    for i in numbers:
        for j in numbers:
            if i != j:
                difference = abs(i - j)
                actual = [i, j, difference]
                results.append(actual)
                if numbers.index(i) == 0 and numbers.index(j) == 1:
                    minDiff = difference
                elif difference < minDiff:
                    minDiff = difference

    goal = []
    for k in results:
        if k[2] == minDiff:
            goal.append(k[0:-1])

    goal.sort()
    for i in goal:
        for j in i:
            sys.stdout.write(str(j)+' ')
        sys.stdout.write('\n')
except ValueError as error:
    sys.stdout.write(error)