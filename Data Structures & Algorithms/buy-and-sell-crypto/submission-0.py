class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        smallest = prices[0]
        profit = 0

        for i in range(len(prices)):
            current = prices[i]
            if profit < current - smallest:
                profit = current - smallest
            elif current < smallest:
                smallest = current
        return profit
            