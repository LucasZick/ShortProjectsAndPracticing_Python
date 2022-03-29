def sum67(nums):
    sum = 0
    counting = True

    for num in nums:
        if num == 6:
            counting = False
        elif num == 7:
            if counting == False:
                counting = True
            else:
                sum = sum + num
        else:
            if counting == True:
                sum = sum + num
            else:
                pass
    
    return sum


print(sum67([2, 7, 6, 2, 6, 7, 2, 7]))
