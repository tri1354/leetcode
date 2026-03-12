class Solution:
    def numberOfSteps(self, num: int) -> int:
        out = 0
        while num: # instead of while num > 0:
            num = num / 2 if num % 2 == 0 else num - 1
            out += 1
        return out