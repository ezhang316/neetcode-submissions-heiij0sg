class Solution:
    def reverse(self, x: int) -> int:
        negative = (x < 0)
        s = abs(x)
        s = str(s)
        s = s[::-1]
        s = int(s)
        print(s)
        if s < -(2**31) or s > 2**31 - 1:
            return 0
        if negative:
            return -s
        return s