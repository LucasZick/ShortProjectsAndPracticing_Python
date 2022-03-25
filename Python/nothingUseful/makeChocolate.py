def make_chocolate(small, big, goal):
    bigsInsideGoal = 0
    bigCount = 0
    for i in range(big):
        if bigsInsideGoal < goal-5:
            bigsInsideGoal+=5
            bigCount+=1

    if goal % 5 == 0 and big*5 >= goal or goal == 0:
        return 0

    elif big*5 + small < goal:
        return -1
    
    else:
        return goal-(bigCount*5)


print(make_chocolate(1000, 1000000, 5000006))