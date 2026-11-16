class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        res = 0
        def combinations(i, j):

            if j == len(t):
                nonlocal res
                res += 1
                return
            
            if i == len(s):
                return

            combinations(i + 1, j)
            if s[i] == t[j]:
                combinations(i + 1, j + 1)
        
        combinations(0,0)
        return res

        