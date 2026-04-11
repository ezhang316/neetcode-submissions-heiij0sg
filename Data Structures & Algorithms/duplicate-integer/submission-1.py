class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        l = []
        for n in nums:
            if n not in l:
                l.append(n)
            else:
                return True

        return False