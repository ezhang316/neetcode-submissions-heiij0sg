class Solution:
    def climbStairs(self, n: int) -> int:
        cur, next = 1, 1
        
        for i in range(n-1):
            temp = next
            next = cur + next
            cur = temp        
        return next

        # 0: 1
        # 1: 1 
        # 2: 2
        # 3: 3
        # 4: 5
        # 5: 8