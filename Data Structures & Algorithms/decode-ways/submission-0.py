class Solution:
    def numDecodings(self, s: str) -> int:
        
        seen = [False for _ in range(len(s))]

        def dfs(i):
            if i >= len(s):
                return 0
            
            if seen[i]:
                return 0
            
            if s[i] == "0":
                return 0

            res = dfs(i + 1)

            if i <= len(s) - 1 and int(s[i:i+2]) <= 26:
                res += dfs(i + 2)

            seen[i] = True

            return res + 1
        
        return dfs(0)
