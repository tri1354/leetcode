class Solution:
    def canJump(self, nums: List[int]) -> bool:
        checkpoint_pos = len(nums)-1
        for i in range(len(nums)-1, -1, -1):
            if nums[i] >= checkpoint_pos - i:
                checkpoint_pos = i
        return checkpoint_pos == 0


        # max_reach = 0
        # for i in range(len(nums)):
        #     if i > max_reach:
        #         return False
        #     max_reach = max(max_reach, nums[i] + i)
        # return True