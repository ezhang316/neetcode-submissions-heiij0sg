class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = []
        
        def rec(i, subset):
            if i == len(nums):
                res.append(subset)
                return
            
            rec(i + 1, subset + [nums[i]])

            cur = nums[i]
            while i < len(nums) and nums[i] == cur:
                i += 1
            
            rec(i, subset)



        rec(0, [])
        return res 