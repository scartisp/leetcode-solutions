class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        maxSum, currSum = nums[0], nums[0]

        for i in range(1, len(nums)):
            if currSum < 0:
                currSum = 0
            currSum += nums[i]
            if maxSum < currSum:
                maxSum = currSum

        return maxSum
