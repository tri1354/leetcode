class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # mod = k%(len(nums))
        # i = len(nums)-1-mod
        # while i >= 0:
        #     j = mod
        #     while j > 0:
        #         nums[i], nums[i+j] = nums[i+j], nums[i]
        #         j -= 1
        #     i -= 1

        left = 0
        right = len(nums) - 1

        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

        mod = k%(len(nums))
        left1 = 0
        right1 = mod - 1

        while left1 < right1:
            nums[left1], nums[right1] = nums[right1], nums[left1]
            left1 += 1
            right1 -= 1

        left2 = mod
        right2 = len(nums) - 1

        while left2 < right2:
            nums[left2], nums[right2] = nums[right2], nums[left2]
            left2 += 1
            right2 -= 1