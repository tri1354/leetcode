class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = [1] * n
        for i in range(1, n): # left -> right
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1] + 1
        for i in range(n-2, -1, -1): # right -> left
            if ratings[i] > ratings[i+1]:
                candies[i] = max(candies[i], candies[i+1] + 1)
        return sum(candies)


        # left_candies = [1] * n
        # right_candies = [1] * n
        # left = 1
        # right = 1
        # for i in range(n-1):
        #     if ratings[i] < ratings[i+1]:
        #         left += 1
        #     else:
        #         left = 1
        #     left_candies[i+1] = left
        # for i in range(n-1, 0, -1):
        #     if ratings[i] < ratings[i-1]:
        #         right += 1
        #     else:
        #         right = 1
        #     right_candies[i-1] = right
        # total_candies = 0
        # for i in range(n):
        #     total_candies += max(left_candies[i], right_candies[i])
        # return total_candies