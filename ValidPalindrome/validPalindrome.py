class Solution:
    def isPalindrome(self, s: str) -> bool:
        sReverse = s[::-1]
        return ''.join([char for char in s if char.isalnum()]).lower() == ''.join([char for char in sReverse if char.isalnum()]).lower() 
