class Solution:
    def maxArea(self, height: List[int]) -> int:
        water = 0
        left = 0
        right = len(height) - 1
        while left < right:
            if height[left] < height[right]:
                water = max(water, height[left] * (right - left))
                left += 1
            else:
                water = max(water, height[right] * (right - left))
                right -= 1
        return water