class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        word_set = set(wordDict)

        memo = [-1 for _ in range(len(s))]

        def dfs(i, j):
            if memo[i] != -1:
                return memo[i]
            
            substring = substring + s[i]

            match = substring in word_set

            res = match and dfs(i + 1)
        return True