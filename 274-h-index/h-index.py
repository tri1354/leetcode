class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # citations.sort(reverse=True)
        # h = 0
        # for i in range(len(citations)):
        #     if citations[i] >= i+1:
        #         h = i+1
        # return h


        n = len(citations)
        count = [0] * (n+1)
        for c in citations:
            if c >= n:
                count[n] += 1
            else:
                count[c] += 1
        h = 0
        for i in range(n, -1, -1):
            h += count[i]
            if h >= i:
                return i
        return 0