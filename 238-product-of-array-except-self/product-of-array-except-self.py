class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n
        right = 1
        for i in range(1, n):
            result[i] = nums[i-1] * result[i-1]
        for i in range(n-2, -1, -1):
            right *= nums[i+1]
            result[i] *= right
        return result