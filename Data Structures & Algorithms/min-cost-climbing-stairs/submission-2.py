class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:

        a, b = 0, 0

        for i in range(len(cost) - 1, -1, -1):
            tmp = a
            a, b = cost[i] + min(a, b), a
            b = tmp
        
        return min(a, b)
