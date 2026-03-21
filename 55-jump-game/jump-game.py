class Solution:
    def canJump(self, nums: List[int]) -> bool:
        checkpoint = 0
        checkpoint_pos = len(nums)-1
        for i in range(len(nums)-1, -1, -1):
            if nums[i] >= checkpoint_pos - i:
                checkpoint_pos = i
                checkpoint = nums[i]
        if checkpoint_pos == 0:
            return True
        else:
            return False