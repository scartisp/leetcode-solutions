class Solution:
    def jump(self, nums: list[int]) -> int:
        dp = [0]*len(nums)

        for i in range(1,len(nums)):
            for j in range(i-1, -1, -1):
                if nums[j] >= i-j:
                    if dp[i] == 0:
                        dp[i] = dp[j] + 1
                    else:
                        dp[i] = min(dp[i], dp[j] + 1)
        
        return dp[-1]
