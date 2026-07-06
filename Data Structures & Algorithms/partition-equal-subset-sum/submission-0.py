class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        nums.sort()
        total = sum(nums)
        if total % 2 == 1:
            return False

        memo = {}
        
        def rec(i, deficit):
            if deficit < -total / 2 or deficit > total / 2:
                return False
            if (i, deficit) in memo:
                return False
            if i == len(nums) - 1:
                return deficit == nums[i]
            
            if rec(i + 1, deficit + nums[i]) or rec(i + 1, deficit - nums[i]):
                return True
            
            memo[(i, deficit)] = False

            return False
        
        return rec(0, 0)

