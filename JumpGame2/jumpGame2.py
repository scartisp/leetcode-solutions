class Solution:
    def jump(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return 0
        numOfJumps = 0
        position = 0
        maxReach = nums[0]
        jumpsLeft = maxReach

        for i in range(1,len(nums)-1):
            if i+nums[i] > position+maxReach:
                maxReach = nums[i]
                position = i
            jumpsLeft -= 1
            if jumpsLeft == 0:
                numOfJumps += 1
                jumpsLeft = maxReach + position - i
        if jumpsLeft > 0:
            numOfJumps += 1
        
        return numOfJumps
