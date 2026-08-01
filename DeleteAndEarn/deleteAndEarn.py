class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        values = [0]*(max(nums)+1)

        for num in nums:
            values[num] += num
        
        earned = [0]*len(values)

        earned[1] = values[1]

        for i in range(2,len(earned)):
            earned[i] = max(values[i]+ earned[i-2], earned[i-1])

        return earned[-1]
