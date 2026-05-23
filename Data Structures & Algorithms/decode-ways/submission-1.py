class Solution:
    def numDecodings(self, s: str) -> int:
        
        memo = [-1 for _ in range(len(s))]

        def dfs(i):
            if i >= len(s):
                return 1
            
            if memo[i] != -1:
                return memo[i]
            
            if s[i] == "0":
                return 0

            res = dfs(i + 1)

            if i <= len(s) - 2 and int(s[i:i+2]) <= 26:
                res += dfs(i + 2)

            memo[i] = res

            return res
        
        return dfs(0)
