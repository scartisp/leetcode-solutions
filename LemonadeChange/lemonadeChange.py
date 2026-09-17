class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        fives = 0
        tens = 0

        for bill in bills:
            if bill == 5:
                fives += 1
            if bill == 10:
                if fives <= 0:
                    return False
                else:
                    fives -= 1
                    tens += 1
            if bill == 20:
                if tens > 0 and fives > 0:
                    fives -= 1
                    tens -= 1
                elif fives >= 3:
                    fives -= 3
                else:
                    return False
        
        return True
