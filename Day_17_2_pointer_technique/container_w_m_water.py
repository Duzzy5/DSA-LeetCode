def bucket(nums):
    left=0
    right=len(nums)-1
    width=left - right
    max_area=0
    while left<right:
        area= ( -left + right) * min(nums[left],nums[right])
        max_area=max(max_area,area)
        
        if nums[left]<nums[right]:
            left+=1
        else:
            right-=1
    return max_area
height = [9,8,7,6,5,4,3,2,1]
print(bucket(height))
