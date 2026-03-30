class Solution:
    def convert(self, s: str, numRows: int) -> str:
        rows = [""] * numRows
        r = numRows - 1
        if r == 0:
            return s
        for i in range(len(s)):
            j = i % (r*2)
            if j <= r:
                rows[j] += s[i]
            else:
                rows[2*r - j] += s[i]
        return "".join(rows)