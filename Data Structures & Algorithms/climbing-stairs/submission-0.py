class Solution:
    def climbStairs(self, n: int) -> int:
        self.count = 0
        self.n = n

        def work_backwards(current_level):
            if current_level < n:
                work_backwards(current_level + 1)
                work_backwards(current_level + 2)
            elif current_level == n:
                self.count += 1
                return
            
            

        work_backwards(0)

        return self.count