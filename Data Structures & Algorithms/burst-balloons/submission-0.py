class Solution:
    def maxCoins(self, nums: List[int]) -> int:

        seen = {}
        
        def rec(nums):
            if len(nums) == 1:
                return nums[0]

            tup = tuple(nums)

            if tup in seen:
                return seen[tup]
            
            processed_max = 0

            for i in range(len(nums)):
                left = 1 if i == 0 else nums[i - 1]
                right = 1 if i == len(nums) - 1 else nums[i + 1]
                balloon_pop = left * nums[i] * right

                new_list = nums[:i] + nums[i + 1:]

                total = balloon_pop + rec(new_list)
                processed_max = max(processed_max, total)
            
            seen[tup] = processed_max

            return seen[tup]
        
        return rec(nums)
            

            