# LeetCode 1480 - Running Sum of 1D Array
# Solved by DUZZY

class Solution(object):
    def runningSum(self, nums):
        ans = []
        s = 0

        for x in nums:
            s = s + x
            ans.append(s)

        return ans
