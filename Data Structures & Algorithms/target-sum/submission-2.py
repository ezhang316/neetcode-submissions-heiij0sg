class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        memo = {}
        def rec(total, i):
            if i == len(nums):
                return 1 if total == target else 0
            if (total, i) in memo:
                return memo[(total, i)]
            
            res1 = rec(total - nums[i], i + 1)
            res2 = rec(total + nums[i], i + 1)

            memo[total,i] = res1 + res2

            return memo[total,i]

        return rec(0, 0)
            
