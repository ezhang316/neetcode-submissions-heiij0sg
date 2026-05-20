class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        def dfs(prev, i):
            if i == len(nums):
                return 0
            
            if memo[prev + 1][i] != -1:
                return memo[prev + 1][i]

            res = dfs(prev, i + 1)
            
            if prev == -1 or nums[prev] < nums[i]:

                res = max(dfs(i, i + 1) + 1, res)
                
            
            memo[prev + 1][i] = res
            return res

        memo = [[-1 for _ in range(len(nums) + 1)] for _ in range(len(nums))]
        
        return dfs(-1,0)
        