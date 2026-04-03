class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_i = 0
        if s == "":
            return True
        for t_i in range(len(t)):
            if t[t_i] == s[s_i]:
                s_i += 1
                if s_i == len(s):
                    return True
        return False