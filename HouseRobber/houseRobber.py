class Solution:
    def rob(self, nums: List[int]) -> int:
        nums.append(0)
        nums.insert(0,0)
        
        profit = [0]*len(nums)
        profit[1] = nums[1]


        for i in range(2,len(profit)):
            profit[i] = max((nums[i]+profit[i-2]), profit[i-1])

        return profit[-1]
