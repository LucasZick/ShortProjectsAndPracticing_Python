def centered_average(nums):
    nums.sort()
    print(nums)
    nums = nums[1:-1]
    return sum(nums)/len(nums)
    #return sum(new) / len(new)


print(centered_average([1,1,1,2,3,1,2,100]))
