class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)
        s[::-1]
        s = int(s)
        if s < -(2^31) or s > 2^31 - 1:
            return 0
        
        return s