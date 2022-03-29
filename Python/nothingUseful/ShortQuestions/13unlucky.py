def sum13(nums):
    sum = 0
    if nums:
        for num in range(len(nums)):
            if num == 0 and nums[num] != 13:
                sum = sum + nums[num]
            elif nums[num] != 13 and nums[num-1] != 13:
                sum = sum + nums[num]
            else:
                continue
        return sum
    else:
        return 0


print(sum13([1, 2, 2, 1]))