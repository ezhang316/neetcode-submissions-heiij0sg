class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        memo = {}
        def combinations(i, j):
            if (i,j) in memo:
                return memo[i,j]

            if j == len(t):
                return 1
            
            if i == len(s):
                return 0

            res = combinations(i + 1, j)
            if s[i] == t[j]:
                res += combinations(i + 1, j + 1)
            
            memo[i,j] = res
            return res
        
        return combinations(0,0)