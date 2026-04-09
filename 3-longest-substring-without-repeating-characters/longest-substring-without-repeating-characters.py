class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        from collections import deque
        window = deque("")
        ans = 0
        for i in range(len(s)):
            while s[i] in window:
                window.popleft()
            window.append(s[i])
            ans = max(ans, len(window))
        return ans