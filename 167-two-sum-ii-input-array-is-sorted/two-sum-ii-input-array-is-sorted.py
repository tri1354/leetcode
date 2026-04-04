class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d = {}
        for i, num in enumerate(numbers):
            remain = target - num
            if remain in d:
                return [d[remain]+1, i+1]
            d[num] = i