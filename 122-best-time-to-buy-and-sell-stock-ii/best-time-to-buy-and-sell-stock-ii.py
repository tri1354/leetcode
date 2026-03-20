class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # prices.insert(0, prices[0])
        # prices.append(prices[-1])

        # min_price = float('inf')
        # profit = 0
        # max_profit = 0

        # for i in range(1, len(prices)-1):
        #     if prices[i] < min_price:
        #         min_price = prices[i]
        #     profit = max(profit, prices[i] - min_price)

        #     if prices[i] <= prices[i-1] and prices[i] < prices[i+1] and i != len(prices)-1:
        #         max_profit -= prices[i]
        #     if prices[i] > prices[i-1] and prices[i] >= prices[i+1] and i != 1:
        #         max_profit += prices[i]
        # return max(profit, max_profit)


        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                max_profit += prices[i] - prices[i-1]
        return max_profit