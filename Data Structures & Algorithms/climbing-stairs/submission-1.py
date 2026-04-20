class Solution:
    def climbStairs(self, n: int) -> int:
        self.seen = {n-1: 1, n-2: 2}

        def work_backwards(current_level):
            if current_level not in self.seen.keys():
                return work_backwards(current_level + 1) + work_backwards(current_level + 2)
            else:
                return self.seen[current_level]
        return work_backwards(0)