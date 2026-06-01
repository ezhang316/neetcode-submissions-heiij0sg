class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        memo = [-1 for _ in range(len(nums))]

        def take_last(i):
            if i >= len(nums):
                return 0
            if memo[i] != -1:
                return memo[i]

            res = 0

            if i == 0:
                res = take_last(i + 1)
            else:
                res = max(take_last(i + 1), take_last(i + 2) + nums[i])
                
            memo[i] = res
            return memo[i]
        
        took_last = take_last(0)

        memo = [-1 for _ in range(len(nums))]

        def leave_last(i):
            if i >= len(nums) - 1:
                return 0
            if memo[i] != -1:
                return memo[i]
            
            res = max(leave_last(i + 1), leave_last(i + 2) + nums[i])
            memo[i] = res
            return res

        left_last = leave_last(0)

        return max(took_last, left_last)