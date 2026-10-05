class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        numSet = set()
        for num in nums:
            if num in numSet:
                return True
            else:
                numSet.add(num)
        return False
