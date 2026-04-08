class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        s = 0
        ans = float('inf')
        for i in range(len(nums)):
            s += nums[i]
            while s >= target:
                ans = min(ans, i - left + 1)
                s -= nums[left]
                left += 1
        return 0 if ans == float('inf') else ans