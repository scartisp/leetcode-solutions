class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        seen = set()
        left = 0
        seen.add(s[left])
        longest = 1
        for i in range(1, len(s)):
            if s[i] not in seen:
                seen.add(s[i])
                longest = max(longest, i - left+1)
            else:
                while s[i] in seen and left < i:
                    seen.remove(s[left])
                    left += 1
                seen.add(s[i])
        
        return longest
