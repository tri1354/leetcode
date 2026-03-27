class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_left = height[left]
        max_right = height[right]
        water = 0
        while left < right:
            if max_left < max_right:
                left += 1
                max_left = max(max_left, height[left])
                water += max_left - height[left]
            else:
                right -= 1
                max_right = max(max_right, height[right])
                water += max_right - height[right]
        return water


        # n = len(height)
        # max_heights = [0] * n
        # max_height = 0
        # for i in range(n):
        #     max_heights[i] = max_height
        #     max_height = max(max_height, height[i])
        # max_height = 0
        # water = 0
        # for i in range(n-1, -1, -1):
        #     water += max(0, min(max_height, max_heights[i]) - height[i])
        #     max_height = max(max_height, height[i])
        # return water


        # n = len(height)
        # water = [0] * n
        # max = 0
        # for i in range(n):
        #     if height[i] > max:
        #         max = height[i]
        #     else:
        #         water[i] = max - height[i]
        # max = 0
        # rain = 0
        # for i in range(n-1, -1, -1):
        #     if height[i] > max:
        #         max = height[i]
        #     else:
        #         rain += min(water[i], max-height[i])
        # return rain