class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count_t = Counter(t)
        window = {}
        have, need = 0, len(count_t)
        res = ""
        res_len = float("inf")
        left = 0
        for right in range(len(s)):
            c = s[right]
            window[c] = window.get(c, 0) + 1
            if c in count_t and window[c] == count_t[c]:
                have += 1
            while have == need:
                if (right - left + 1) < res_len:
                    res = s[left:right+1]
                    res_len = right - left + 1
                window[s[left]] -= 1
                if s[left] in count_t and window[s[left]] < count_t[s[left]]:
                    have -= 1
                left += 1
        return res