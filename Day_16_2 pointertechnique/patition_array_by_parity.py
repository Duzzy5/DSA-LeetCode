def pabyp(nums):
    j = 0
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            nums[j], nums[i] = nums[i], nums[j]
            j += 1
    return nums
#example
nums=[8,3,6,1,4]
print(pabyp(nums))
