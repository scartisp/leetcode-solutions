class Solution:
    def numDecodings(self, s: str) -> int:
        cache = [0]*(len(s)+1)
        if s[0] == '0':
            return 0
        cache[0] = 1
        cache[1] = 1

        for i in range(1, len(s)):
            oneDigit = int(s[i])
            twoDigit = int(s[i-1])*10 + int(s[i])

            if oneDigit >= 1:
                cache[i+1] += cache[i]
            if 10 <= twoDigit <= 26 and twoDigit:
                cache[i+1] +=  cache[i-1]
        
        return cache[-1]
