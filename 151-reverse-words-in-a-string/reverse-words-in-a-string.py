class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.split()
        s=s[::-1]
        return " ".join(s)

        
        # temp_words = [""]
        # for c in s:
        #     if c != " ":
        #         temp_words[-1] += c
        #     else:
        #         if temp_words[-1] != "":
        #             temp_words.append("")
        # if temp_words[-1] == "":
        #     temp_words.pop()
        # ans = ""
        # for i in range(len(temp_words)-1, -1, -1):
        #     ans += temp_words[i]
        #     ans += " "
        # ans = ans[:-1]
        # return ans