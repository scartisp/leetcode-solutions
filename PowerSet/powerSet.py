class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        subsets = []
        subsets.append([])
        for num in nums:
            subsetsCount = len(subsets)
            for i in range(subsetsCount):
                subset = subsets[i].copy()
                subset.append(num)
                subsets.append(subset)

        return subsets
