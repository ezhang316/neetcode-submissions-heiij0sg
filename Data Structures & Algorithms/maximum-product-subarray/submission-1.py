class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = -math.inf

        def dfs(smallest, largest, i):
            if i >= len(nums):
                return 0
            
            current_pos = nums[i] * largest
            current_unsure = nums[i] * smallest

            new_largest = max(current_pos, current_unsure)
            new_smallest = min(current_pos, current_unsure)
            
            if largest == 0:
                new_largest = new_smallest = nums[i]

            nonlocal res
            res = max(res, new_largest)

            dfs(new_smallest, new_largest, i + 1)
    
        dfs(0,0,0)
        return res