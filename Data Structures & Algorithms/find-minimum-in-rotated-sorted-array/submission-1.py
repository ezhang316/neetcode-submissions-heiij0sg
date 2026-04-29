class Solution:
    def findMin(self, nums: List[int]) -> int:

        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if nums[l] < nums[r]:
                return nums[l]
            else:
                if nums[r - 1] > nums[r]:
                    return nums[r]
                elif nums[m - 1] > nums[m]:
                    return nums[m]
                else:
                    if nums[l] < nums[m]:
                        l = m + 1
                    else:
                        r = m - 1
        
        return nums[l]