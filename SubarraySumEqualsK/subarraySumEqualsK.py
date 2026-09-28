class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixDict = {0:1}
        cur = ans = 0
        for num in nums:
            cur += num
            ans += prefixDict.get(cur-k,0)
            prefixDict[cur] = prefixDict.get(cur,0)+1
        
        return ans


        
