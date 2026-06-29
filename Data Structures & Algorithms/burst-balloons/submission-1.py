class Solution:
    def maxCoins(self, nums: List[int]) -> int:

        nums = [1] + nums + [1]
        seen = {}
        
        def rec(l, r):
            if l > r:
                return 0

            if (l, r) in seen:
                return seen[(l, r)]
            
            processed_max = 0

            for i in range(l, r + 1):
                balloon_pop = nums[l - 1] * nums[i] * nums[r + 1]
                total = rec(l, i - 1) + balloon_pop + rec(i + 1, r)
                processed_max = max(processed_max, total)
            
            seen[(l, r)] = processed_max

            return seen[(l, r)]
        
        return rec(1, len(nums) - 2)
            

            