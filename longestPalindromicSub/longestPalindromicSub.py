class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        left = -1
        right = -1
        longestSub = ''

        for i in range(len(s),):
            left = i-1
            right = i+1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if len(longestSub) < right - left + 1:
                    longestSub = s[left:right+1]
                left -= 1
                right += 1
            
            left = i
            right = i+1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if len(longestSub) < right - left + 1:
                    longestSub = s[left:right+1]
                left -= 1
                right += 1
            
        
        if longestSub == '':
            return s[-1]
        else:
            return longestSub
