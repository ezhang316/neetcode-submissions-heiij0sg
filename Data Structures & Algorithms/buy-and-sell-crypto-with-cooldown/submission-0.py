class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = [-1 for _ in range(len(prices))]

        def rec(i):
            if i >= len(prices):
                return 0
            if memo[i] != -1:
                return memo[i]
            
            skip = rec(i + 1)

            buy_and_sell = 0

            for j in range(i, len(prices)):
                cur = -prices[i] + prices[j] + rec(j + 2)
                buy_and_sell = max(buy_and_sell, cur)
            
            memo[i] = max(skip, buy_and_sell)

            return memo[i]

        return rec(0)