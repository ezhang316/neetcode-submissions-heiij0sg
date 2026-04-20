class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r)//2

            if nums[m] == target:
                return m
            elif nums[l] < nums[r]: # no break in search area
                if nums[m] > target:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if nums[m] < nums[l]: # break is on left side of m
                    if nums[m] > target:
                        r = m - 1
                    else:
                        if nums[r] < target:
                            r = m - 1
                        else:
                            l = m + 1
                else: # break is on right side of m
                    if nums[m] < target:
                        l = m + 1
                    else:
                        if nums[l] > target:
                            l = m + 1
                        else:
                            r = m - 1

        return -1