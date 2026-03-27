class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        water = [0] * n
        max = 0
        for i in range(n):
            if height[i] > max:
                max = height[i]
            else:
                water[i] = max - height[i]
        max = 0
        rain = 0
        for i in range(n-1, -1, -1):
            if height[i] > max:
                max = height[i]
            else:
                rain += min(water[i], max-height[i])
        return rain