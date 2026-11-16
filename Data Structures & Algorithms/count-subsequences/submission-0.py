class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        res = 0
        seen = set()
        def combinations(i, j):
            nonlocal seen
            if (i,j) in seen:
                return
            if j == len(t):
                nonlocal res
                res += 1
                seen.add((i,j))
                return
            
            if i == len(s):
                seen.add((i,j))
                return

            combinations(i + 1, j)
            if s[i] == t[j]:
                combinations(i + 1, j + 1)
        
        combinations(0,0)
        return res

        