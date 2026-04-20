class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r)//2

            if nums[m] == target:
                return m
            if nums[l] == target:
                return l
            if nums[r] == target:
                return r
            
            if nums[l] < nums[r]: # no break
                if nums[m] > target:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if nums[m] < nums[l]: # break is on left side
                    if nums[m] > target:
                        r = m - 1
                    else:
                        if nums[r] < target:
                            r = m - 1
                        else:
                            l = m + 1
                else: # break is on right side
                    if nums[m] < target:
                        l = m + 1
                    else:
                        if nums[l] > target:
                            l = m + 1
                        else:
                            r = m - 1

        return -1