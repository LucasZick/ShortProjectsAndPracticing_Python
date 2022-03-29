def big_diff(nums):
    maxim = max(nums)
    minim = min(nums)
    return(abs(maxim-minim))

print(big_diff([10, 3, 5, 6,2,1,31,1,23,12,3,13,12,3,45,435,46,3,534,1,3,31,3,4,3,45,4,5,6,3,23,3,4,35,56,4,]))