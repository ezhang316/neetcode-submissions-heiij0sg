class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        res = 0
        memo = {}
        def rec(total, i):
            if (total, i) in memo:
                return memo[(total, i)]
            if i == len(nums):
                if total == target:
                    nonlocal res
                    res += 1
                    memo[total,i] = 1
                else:
                    memo[total,i] = 0
                return memo[total,i]
            
            res1 = rec(total - nums[i], i + 1)
            res2 = rec(total + nums[i], i + 1)

            memo[total,i] = res1 + res2

            return memo[total,i]

        return rec(0, 0)
            
