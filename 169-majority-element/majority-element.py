class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # d = {}
        # for num in nums:
        #     d[num] = d.get(num, 0) + 1
        # return max(d, key=d.get)

        # Boyer–Moore
        ans = 0
        count = 0

        for num in nums:
            if count == 0:
                ans = num
            count += (1 if num == ans else -1)
        
        return ans