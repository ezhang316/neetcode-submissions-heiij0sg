class Solution:
    def canJump(self, nums: List[int]) -> bool:
        can = {}

        def rec(index):
            print(index)
            if index >= len(nums) - 1:
                return True
            if index not in can:
                for i in range(nums[index], 0, -1):
                    if index + i in can:
                        return can[index + 1]
                    can[index + i] = ret = rec(index + i)
                    if ret:
                        return ret
            else:
                return can[index]
            can[index] = False
            return False
        
        return rec(0)

