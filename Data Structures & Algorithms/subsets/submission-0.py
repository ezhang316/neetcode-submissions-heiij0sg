class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def rec(i, cur):
            if i >= len(nums):
                res.append(cur.copy())
                return
            
            rec(i + 1, cur)

            cur.append(nums[i])
            rec(i + 1, cur)
            cur.pop()

        rec(0, [])
        return res
