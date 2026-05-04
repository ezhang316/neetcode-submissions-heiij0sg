class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        res = -math.inf

        current = 0

        for i in range(len(nums)):
            current += nums[i]

            if current < nums[i]:
                current = nums[i]
            print(current)
            res = max(res, current)

        return res