class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sPointer = 0
        tPointer = 0
        while sPointer < len(s) and tPointer < len(t):
            if t[tPointer] == s[sPointer]:
                sPointer += 1
            tPointer += 1
        return sPointer == len(s)
