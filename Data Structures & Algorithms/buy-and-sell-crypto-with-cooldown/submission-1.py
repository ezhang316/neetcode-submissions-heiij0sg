class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}

        def rec(i, b):
            if i >= len(prices):
                return 0
            if (i, b) in memo:
                return memo[i,b]
            
            skip = rec(i + 1, b)

            if b:
                cur = -prices[i] + rec(i + 1, not b)
            else:
                cur = prices[i] + rec(i + 2, not b)
            
            memo[i,b] = max(skip, cur)

            return memo[i,b]

        return rec(0,True)