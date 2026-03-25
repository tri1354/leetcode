class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # n = len(nums)
        # result = [1] * n
        # right = 1
        # for i in range(1, n):
        #     result[i] = nums[i-1] * result[i-1]
        # for i in range(n-2, -1, -1):
        #     right *= nums[i+1]
        #     result[i] *= right
        # return result


        result = []
        product = 1
        for num in nums:
            result.append(product)
            product *= num
        product = 1
        for i in range(len(nums)-1, -1, -1):
            result[i] *= product
            product *= nums[i]
        return result