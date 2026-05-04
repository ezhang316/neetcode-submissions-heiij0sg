class Solution:
    def canJump(self, nums: List[int]) -> bool:
        can = {}

        def rec(index):
            print(index)
            if index >= len(nums) - 1:
                return True
            if index not in can:
                for i in range(1, nums[index] + 1):
                    can[index + i] = ret = rec(index + i)
                    if ret:
                        return ret
            else:
                return can[index]
            return False
        
        return rec(0)

