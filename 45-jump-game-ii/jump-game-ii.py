class Solution:
    def jump(self, nums: List[int]) -> int:
        steps = 0
        checkpoint_pos = 0
        checkpoint = nums[0]
        if checkpoint_pos == len(nums)-1:
            return 0
        while checkpoint < len(nums)-1:
            temp = checkpoint
            temp_pos = checkpoint_pos
            for i in range(temp_pos, temp+1):
                if nums[i]+i > checkpoint:
                    checkpoint = nums[i]+i
                    checkpoint_pos = i
            steps += 1
        return steps + 1


        # steps = 0
        # checkpoint_pos = 0
        # checkpoint = 0
        # if checkpoint_pos == len(nums)-1:
        #     return 0
        # for i in range(len(nums)):
        #     if nums[i]+i >= len(nums)-1:
        #         steps += 1
        #         break
        #     else:
        #         if nums[i]+i > checkpoint+checkpoint_pos:
        #             checkpoint_pos = i
        #             checkpoint = nums[i]
        #             steps += 1
        #         if i+checkpoint < len(nums):
        #             if checkpoint_pos+checkpoint + nums[checkpoint_pos+checkpoint] >= len(nums)-1:
        #                 steps += 1
        #                 break 
        # return steps