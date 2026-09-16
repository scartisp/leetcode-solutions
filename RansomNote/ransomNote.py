class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazineCount = Counter(magazine)

        for char in ransomNote:
            if char not in magazineCount or magazineCount[char] == 0:
                return False
            magazineCount[char] -= 1
        
        return True
