class Solution:
    def jump(self, nums: List[int]) -> int:
        # steps = 0
        # checkpoint_pos = 0
        # checkpoint = nums[0]
        # if checkpoint_pos == len(nums)-1:
        #     return 0
        # while checkpoint < len(nums)-1:
        #     temp = checkpoint
        #     temp_pos = checkpoint_pos
        #     for i in range(temp_pos, temp+1):
        #         if nums[i]+i > checkpoint:
        #             checkpoint = nums[i]+i
        #             checkpoint_pos = i
        #     steps += 1
        # return steps + 1


        steps = 0
        end = 0
        farthest = 0
        for i in range(len(nums)-1):
            farthest = max(farthest, nums[i]+i)
            if i == end:
                steps += 1
                end = farthest
        return steps