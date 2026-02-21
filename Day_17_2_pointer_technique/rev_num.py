#reverse an array
def rev_num(nums):
    left=0
    right=len(nums)-1
    while left<right:
        nums[left],nums[right]= nums[right],nums[left]
        left+=1
        right-=1
    return nums

nums =[1,2,3,4,5,6]
print(rev_num(nums))
