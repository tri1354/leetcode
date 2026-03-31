class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # return haystack.find(needle)

        # this way is no different than brute-force way and i hate it
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1