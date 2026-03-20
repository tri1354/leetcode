class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # max_profit = 0
        # if len(prices) < 3:
        #     if len(prices) == 2:
        #         max_profit = prices[1] - prices[0]
        #         return max_profit if max_profit > 0 else 0
        #     else:
        #         return 0
        # else:
        #     for i in range(1, len(prices) - 1):
        #         min_price1 = float('inf')
        #         profit1 = 0
        #         for j in range(i):
        #             if prices[j] < min_price1:
        #                 min_price1 = prices[j]
        #             profit1 = max(profit1, prices[j] - min_price1)
                
        #         min_price2 = float('inf')
        #         profit2 = 0
        #         for k in range(i-1, len(prices)):
        #             if prices[k] < min_price2:
        #                 min_price2 = prices[k]
        #             profit2 = max(profit2, prices[k] - min_price2)

        #         max_profit = max(max_profit, profit1 + profit2)
        # return max_profit


        n = len(prices)
        if n < 2:
            return 0
        
        left = [0] * n
        right = [0] * n

        min_price = prices[0]
        for i in range(1, n):
            min_price = min(min_price, prices[i])
            left[i] = max(left[i-1], prices[i] - min_price)

        max_price = prices[-1]
        for i in range(n-2, -1, -1):
            max_price = max(max_price, prices[i])
            right[i] = max(right[i+1], max_price - prices[i])

        max_profit = 0
        for i in range(n):
            max_profit = max(max_profit, left[i] + right[i])

        return max_profit