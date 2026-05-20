class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        def dfs(prev, i):
            if i == len(nums):
                return 0
            
            if (prev,i) in memo:
                return memo[(prev,i)]
            
            if prev == -1 or nums[prev] < nums[i]:

                res = max(dfs(i, i + 1) + 1, dfs(prev, i + 1))

            else:
                res = dfs(prev, i + 1)
            
            memo[prev, i] = res
            return res
        # res = 0
        # for i in range(len(nums)):
        memo = {}
        #     res = max(res, dfs(-1, i))
        
        return dfs(-1,0)
        