class Solution:
    def compress(self, chars: list[str]) -> int:
        s = []
        character = ''
        count = 0
        for char in chars:
            if char != character:
                if character != '':
                    s.append(character)
                    if count > 1:
                        countList = []
                        while count > 0:
                            countList.append(str(count%10))
                            count //= 10
                        for countChar in reversed(countList): s.append(countChar)
                character = char
                count = 1
            else:
                count += 1
        
        s.append(character)
        if count > 1:
            countList = []
            while count > 0:
                countList.append(str(count%10))
                count //= 10
            for countChar in reversed(countList): s.append(countChar)

        for char in reversed(s):
            chars.insert(0,char)

        return len(s)
            
