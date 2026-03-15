class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        j = len(nums)-1

        while i <= j:
            if nums[i] == val and nums[j] != val:
                nums[i], nums[j] = nums[j], nums[i]
            if nums[i] != val:
                i += 1
            if nums[j] == val:
                j -= 1
        
        return j+1