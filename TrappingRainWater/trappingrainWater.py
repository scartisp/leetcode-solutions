class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        tempCount = 0
        count = 0

        while(left < len(height) and height[left] == 0):
            left += 1
        for i in range(left+1,len(height)):
            if height[i] < height[left]:
                tempCount += height[left] - height[i]
            elif height[i] >= height[left]:
                count += tempCount
                left = i
                tempCount = 0 
        
        if left < len(height)-2:
            tempCount = 0
            right = len(height)-1
            for i in range(len(height)-2, left,-1):
                if height[i] > height[right]:
                    right = i
                elif height[i] < height[right]:
                    tempCount += height[right]-height[i]
            
            count += tempCount
        
        return count
