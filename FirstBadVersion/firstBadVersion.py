# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n
        firstBad = -1

        while left < right-1:
            middle = left + (right-left)//2
            if isBadVersion(middle):
                right = middle
            else:
                left = middle

        if isBadVersion(left):
            return left
        return right
