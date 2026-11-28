class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        memo = [-1 for _ in range(len(cost) + 2)]
        memo[len(cost)] = 0
        memo[len(cost) + 1] = 0

        def rec(i):
            if memo[i] != -1:
                return  memo[i]
            
            memo[i] = min(rec(i + 1) + cost[i], rec(i + 2) + cost[i])

            return memo[i]
        
        return min(rec(0), rec(1))
