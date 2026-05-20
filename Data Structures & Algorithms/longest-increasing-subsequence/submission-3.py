class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        def dfs(prev, i):
            if i == len(nums):
                return 0

            print(nums[prev], nums[i])
            
            if memo[i] != -1:
                return memo[i]
            
            if prev == -1 or nums[prev] < nums[i]:

                res = max(dfs(i, i + 1) + 1, dfs(prev, i + 1))
                memo[i] = res

            else:
                res = dfs(prev, i + 1)
            
            return res
        # res = 0
        # for i in range(len(nums)):
        memo = [-1 for _ in range(len(nums))]
        #     res = max(res, dfs(-1, i))
        
        return dfs(-1,0)
        