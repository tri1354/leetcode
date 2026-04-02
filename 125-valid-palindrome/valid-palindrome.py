class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = "".join(c for c in s if c.isalnum()).lower()
        return result == result[::-1]


        # n = len(result) - 1
        # if result == "":
        #     return True
        # for i in range(len(result)//2):
        #     if result[i] != result[n-i]:
        #         return False
        # return True