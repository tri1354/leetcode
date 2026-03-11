class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        # customer_wealths = []
        # for i in accounts:
        #     total_money = 0
        #     for j in i:
        #         total_money += j
        #     customer_wealths.append(total_money)
        # return max(customer_wealths)

        # customer_wealths = []
        # for customer in accounts:
        #     customer_wealths.append((sum(customer)))
        # return max(customer_wealths)

        return max(sum(customer) for customer in accounts)