class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        i = 0
        currMax = [0] * len(nums)
        currMax[i] = nums[i]

        for j in range(i+1, len(nums)):
            currMax[j] = max(nums[j], currMax[j-1]+nums[j])
        
        return max(currMax)
