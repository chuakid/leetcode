class Solution:
    def maxSubArray(self, nums) -> int:
        currMax = nums[0]
        totalMax = nums[0]
        for i in nums[1:]:
            currMax = max(i, currMax + i)
            totalMax = max(currMax, totalMax)
        return totalMax
