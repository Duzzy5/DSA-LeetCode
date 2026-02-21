def tsum(nums,target):
    left=0
    right=len(nums)-1
    while left<right:
        if (nums[left]+nums[right])>target:
            right -=1
        elif (nums[left]+nums[right])<target:
            left +=1
        else:
            return left+1,right+1
            

numbers = [1,2,3,4,6]
target = 6  
print(tsum(numbers,target))
