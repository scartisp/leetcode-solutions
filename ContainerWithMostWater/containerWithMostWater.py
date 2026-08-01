class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        maxWater = (right-left)*min(height[left],height[right])
        while (left < right and right >= 0 and left < len(height)):
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            maxWater = max(maxWater, (right-left)*min(height[left],height[right]))
        
        return maxWater
