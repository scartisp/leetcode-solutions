class Solution:
    def canJump(self, nums: list[int]) -> bool:
        location = 0
        jump = nums[location]
        while True:
            if location + jump >= len(nums)-1:
                return True
            if nums[location] == 0:
                return False
            nextJump = nums[location+1]
            nextLocation = location + 1
            for i in range(2, jump+1):
                if nums[location+i]+location+i >= nextJump+nextLocation:
                    nextJump = nums[location+i]
                    nextLocation = location + i
            jump = nextJump
            location = nextLocation
