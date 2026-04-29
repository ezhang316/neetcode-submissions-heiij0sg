class Solution:
    def rob(self, nums: List[int]) -> int:

        seen = {}
        
        def dfs(i):
            if i >= len(nums):
                return 0
            
            if i in seen.keys():
                return seen[i]

            value = max(dfs(i + 2) + nums[i], dfs(i + 1))

            seen[i] = value

            return seen[i]
        
        return dfs(0)