class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        memo = [-1 for _ in range(len(s))]

        def dfs(i):
            if i == len(s):
                return True
            if memo[i] != -1:
                return memo[i]
            
            for word in wordDict:
                j = i + len(word)
                if j <= len(s) and s[i:j] == word and dfs(j):
                    return True
            memo[i] = 0
            return False
        
        return dfs(0)