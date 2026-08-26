class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0]*len(temperatures)
        stack = [(temperatures[0], 0)]

        for i in range (1, len(temperatures)):
            while stack and stack[-1][0] < temperatures[i]:
                temp, index = stack.pop()
                output[index] = i-index 
            stack.append((temperatures[i], i))
        
        return output
