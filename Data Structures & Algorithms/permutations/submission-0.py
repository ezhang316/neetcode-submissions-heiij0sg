class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def rec(nums, current):
            if not nums:
                return res.append(list(current))

            it = list(nums)

            for n in it:
                nums.remove(n)
                current.append(n)
                rec(nums, current)
                nums.add(n)
                current.pop()
        
        rec(set(nums), [])

        return res