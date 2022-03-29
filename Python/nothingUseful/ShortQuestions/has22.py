def has22(nums):
    string = ''
    for num in nums:
        string = string + str(num)
    if '22' in string:
        return True
    else:
        return False

print(has22([1, 2, 2]))
print(has22([1, 2, 1, 2]))