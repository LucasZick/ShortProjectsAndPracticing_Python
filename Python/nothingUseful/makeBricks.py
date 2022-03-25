def make_bricks(small, big, goal):
    if small > goal:
        return True
    elif goal % 5 == 0 and big * 5 >= goal:
        return True
    elif goal == 0:
        return True
    else:
        if (big*5)+small >= goal and goal%5 <= small:
            return True
        else: 
            return False


print(make_bricks(3,1,10))