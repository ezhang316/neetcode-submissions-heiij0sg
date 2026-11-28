class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        memo = [-1 for _ in range(len(cost))]

        def rec(i):
            if i >= len(cost):
                return 0
            if memo[i] != -1:
                return  memo[i]
            
            memo[i] = min(rec(i + 1) + cost[i], rec(i + 2) + cost[i])

            return memo[i]
        
        return min(rec(0), rec(1))
